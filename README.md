# BlurGuard

BlurGuard is a powerful, user-friendly application built with Streamlit that provides automated face anonymization for images and videos. It uses advanced face detection technology to identify and blur faces while preserving the overall quality of your media content.

## Features

- **Advanced Face Detection**: Utilizes the YuNet face detection model for accurate face identification
- **Dual Media Support**: Process both images and videos in popular formats
- **Adjustable Anonymization**: Customize blur intensity to match your privacy requirements
- **Batch Processing**: Handle multiple faces in a single media file
- **User-Friendly Interface**: Clean, intuitive web interface built with Streamlit
- **Instant Preview**: See the results of face anonymization in real-time
- **Download Options**: Easily save and download processed media files

## Supported Formats

- **Images**: JPG, JPEG, PNG
- **Videos**: MP4, AVI, MOV

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blurguard.git
cd blurguard
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Download the YuNet face detection model:
```bash
Download face_detection_yunet_2023mar.onnx from this repo
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Access the web interface through your browser (typically http://localhost:8501)

3. Choose between image or video processing using the tabs

4. Upload your media file and adjust the blur intensity using the sidebar slider

5. Click the process button and download your anonymized media

## Requirements

- Python 3.7+
- OpenCV (cv2)
- Streamlit
- NumPy
- Pillow

## Technical Details

BlurGuard uses OpenCV's YuNet face detector, which offers:
- High accuracy face detection
- Support for multiple face detection in a single frame
- Efficient processing suitable for both images and videos
- CPU-based processing requiring no specialized hardware

## Privacy Considerations

- All processing is done locally on your machine
- No data is stored permanently unless you download the processed files
- Temporary files are automatically cleaned up after processing

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- OpenCV for the YuNet face detection model
- Streamlit for the web application framework

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.
