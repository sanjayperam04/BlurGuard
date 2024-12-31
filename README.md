# BlurGuard

> Advanced privacy protection through automated face anonymization in images and videos

## Overview

BlurGuard is a powerful, user-friendly application that provides automated face anonymization for images and videos. Built with Streamlit and powered by the YuNet face detection model, it offers enterprise-grade privacy protection without compromising on simplicity.

## Features

### Core Capabilities
- Automated face detection and blurring using YuNet model
- Support for both images (JPG, JPEG, PNG) and videos (MP4, AVI, MOV)
- Local processing for enhanced security
- Real-time preview of anonymization results
- Customizable blur intensity
- Batch processing support

### Security & Privacy
- All processing performed locally on user's device
- No cloud storage or external data transmission
- Automatic cleanup of temporary files
- Complete user control over media content

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Dependencies:
  - OpenCV (cv2)
  - Streamlit
  - NumPy
  - Pillow

### Quick Start
1. Visit [blurguard.streamlit.app](http://blurguard.streamlit.app)
2. Upload your media file
3. Adjust blur settings using the intensity slider
4. Process and download your anonymized content

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sanjayperam04/BlurGuard.git
cd BlurGuard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

### Image Processing
1. Select the "Image Processing" tab
2. Upload an image (JPG, JPEG, or PNG)
3. Adjust the blur intensity using the slider
4. Click "Apply Face Blurring"
5. Download the processed image

### Video Processing
1. Select the "Video Processing" tab
2. Upload a video (MP4, AVI, or MOV)
3. Adjust the blur intensity
4. Click "Process Video"
5. Download the anonymized video

## Contributing

We welcome contributions from the community. To contribute:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Submit a pull request

Please ensure your code adheres to our coding standards and includes appropriate tests.

## License

BlurGuard is released under the MIT License. See [LICENSE](LICENSE) for details.

## Support

- **Issues & Bugs**: Submit via our [GitHub repository](https://github.com/sanjayperam04/BlurGuard)
- **Documentation**: Available in our [GitHub wiki](https://github.com/sanjayperam04/BlurGuard/wiki)
- **Feature Requests**: Use the Issues section with the 'enhancement' label

## Project Status

BlurGuard is under active development. We regularly release updates with new features and improvements.

---

*BlurGuard: Empowering privacy protection in the digital age.*
