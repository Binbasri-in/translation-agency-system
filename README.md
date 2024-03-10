[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H5VAL6E)

# Translation Agency System

The Translation Agency System is a sophisticated platform designed for translation agencies, aimed at enhancing the efficiency and effectiveness of translating text and documents. Built on the Django framework and leveraging the Cloudflare AI API, this system brings the power of artificial intelligence directly to your translation workflows, automating processes and providing high-quality translations.

## Features

- **Cloudflare AI API Integration**: Harness the capabilities of Cloudflare AI for fast and accurate translations.
- **Built with Django**: A robust and scalable web framework that ensures a seamless user experience.
- **User-Friendly Interface**: Manage translation projects with an intuitive UI designed for ease of use.
- **API for Automation**: Utilize the system's API for integrating translation capabilities into your existing infrastructure, enabling automated translation workflows.

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Django 3.2 or newer
- Access to Cloudflare AI API

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Binbasri-in/translation-agency-system.git
   ```

2. Navigate to the project directory:
   ```
   cd translation-agency-system
   ```

3. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Migrate the database:
   ```
   python manage.py migrate
   ```

5. Start the Django development server:
   ```
   python manage.py runserver
   ```

The server will start, and you can access the application at `http://127.0.0.1:8000`.

## Usage

- **Translating Text**: Use the system's web interface to input text or upload documents for translation.
- **API Interaction**: Leverage the API for programmatically submitting translation requests and retrieving results.

## Roadmap

- [x] Development of a user-friendly web interface using Django.
- [x] Integrating OCR technology for reading text from PDF and Images
- [x] Support different file types (PDF, Image) as input and (Word, Excel, Text) as output
- [x] Deploy the app in Heroku
- [x] Integration with Cloudflare AI API for text and document translations.
- [ ] Advanced feature development and integration with additional AI models for improved translation accuracy and capabilities.

## Contributing

We welcome contributions to the Translation Agency System! Whether it's feature suggestions, bug reports, or code contributions, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
