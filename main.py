import streamlit as st
import numpy as np
import cv2 as cv
from PIL import Image
import tempfile

# Set page configuration
st.set_page_config(
    page_title="Face Anonymizer Pro",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main > div {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .css-1d391kg {
        padding: 2rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def blur_faces(image, blur_level):
    # Function implementation stays the same as in original code
    model_path = 'face_detection_yunet_2023mar.onnx'
    yunet = cv.FaceDetectorYN.create(
        model=model_path,
        config='',
        input_size=(320, 320),
        score_threshold=0.6,
        nms_threshold=0.3,
        top_k=5000,
        backend_id=cv.dnn.DNN_BACKEND_DEFAULT,
        target_id=cv.dnn.DNN_TARGET_CPU
    )

    image_cv = np.array(image)
    image_cv = cv.cvtColor(image_cv, cv.COLOR_RGB2BGR)

    yunet.setInputSize((image_cv.shape[1], image_cv.shape[0]))
    _, faces = yunet.detect(image_cv)

    if faces is not None:
        for face in faces:
            coords = face[:-1].astype(np.int32)
            x, y, w, h = coords[0], coords[1], coords[2], coords[3]
            face_region = image_cv[y:y+h, x:x+w]
            blurred_face = cv.GaussianBlur(face_region, (blur_level, blur_level), 30)
            image_cv[y:y+h, x:x+w] = blurred_face

    image_cv = cv.cvtColor(image_cv, cv.COLOR_BGR2RGB)
    return image_cv

def blur_faces_in_video(video_path, blur_level):
    # Function implementation stays the same as in original code
    model_path = 'face_detection_yunet_2023mar.onnx'
    yunet = cv.FaceDetectorYN.create(
        model=model_path,
        config='',
        input_size=(320, 320),
        score_threshold=0.6,
        nms_threshold=0.3,
        top_k=5000,
        backend_id=cv.dnn.DNN_BACKEND_DEFAULT,
        target_id=cv.dnn.DNN_TARGET_CPU
    )

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        return None

    frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv.CAP_PROP_FPS))
    fourcc = cv.VideoWriter_fourcc(*'mp4v')

    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    output_path = temp_output.name

    out = cv.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        yunet.setInputSize((frame.shape[1], frame.shape[0]))
        _, faces = yunet.detect(frame)
        if faces is not None:
            for face in faces:
                coords = face[:-1].astype(np.int32)
                x, y, w, h = coords[0], coords[1], coords[2], coords[3]
                x = max(0, x)
                y = max(0, y)
                w = min(frame.shape[1] - x, w)
                h = min(frame.shape[0] - y, h)

                if w > 0 and h > 0:
                    face_region = frame[y:y+h, x:x+w]
                    blurred_face = cv.GaussianBlur(face_region, (blur_level, blur_level), 30)
                    frame[y:y+h, x:x+w] = blurred_face

        out.write(frame)

    cap.release()
    out.release()
    return output_path

def main():
    # Sidebar configuration
    with st.sidebar:
        st.title("Settings")
        
        blur_level = st.slider(
            "Blur Intensity",
            min_value=3,
            max_value=99,
            value=21,
            step=2,
            help="Higher values create stronger blur effect. Must be odd numbers."
        )
        
        st.markdown("---")
        st.markdown("""
        ### About
        Face Anonymizer Pro helps you protect privacy by automatically detecting and blurring faces in images and videos.
        
        ### Features
        - Advanced face detection
        - Adjustable blur intensity
        - Supports images & videos
        - Instant processing
        """)

    # Main content
    st.title("Face Anonymizer Pro")
    st.markdown("""
        Protect privacy in your media content with professional-grade face anonymization.
        Upload your files below to get started.
    """)

    # Create tabs for Image and Video processing
    tab1, tab2 = st.tabs(["📷 Image Processing", "🎥 Video Processing"])

    with tab1:
        st.header("Image Anonymization")
        uploaded_image = st.file_uploader(
            "Upload an image file",
            type=["jpg", "jpeg", "png"],
            help="Supported formats: JPG, JPEG, PNG"
        )

        if uploaded_image:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Original Image")
                image = Image.open(uploaded_image)
                st.image(image, use_container_width=True)

            with col2:
                st.subheader("Processed Image")
                if st.button("Apply Face Blurring", key="blur_image"):
                    with st.spinner("Processing image..."):
                        blurred_image = blur_faces(image, blur_level)
                        st.image(blurred_image, use_container_width=True)
                        
                        # Save and provide download option
                        result_image = Image.fromarray(blurred_image)
                        result_image.save("blurred_image.png")
                        with open("blurred_image.png", "rb") as file:
                            st.download_button(
                                "📥 Download Processed Image",
                                file,
                                "blurred_image.png",
                                "image/png",
                                use_container_width=True
                            )

    with tab2:
        st.header("Video Anonymization")
        uploaded_video = st.file_uploader(
            "Upload a video file",
            type=["mp4", "avi", "mov"],
            help="Supported formats: MP4, AVI, MOV"
        )

        if uploaded_video:
            st.video(uploaded_video)
            if st.button("Process Video", key="blur_video"):
                with st.spinner("Processing video... This may take a few minutes."):
                    # Save uploaded video temporarily
                    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
                    temp_video.write(uploaded_video.read())
                    temp_video.close()

                    # Process the video
                    output_path = blur_faces_in_video(temp_video.name, blur_level)
                    if output_path:
                        st.success("✅ Video processing complete!")
                        with open(output_path, "rb") as file:
                            st.download_button(
                                "📥 Download Processed Video",
                                file,
                                "anonymized_video.mp4",
                                "video/mp4",
                                use_container_width=True
                            )
                    else:
                        st.error("❌ Failed to process the video. Please try again.")

    # Footer
    st.markdown("---")
   

if __name__ == "__main__":
    main()