// Configuration for the Resume Analyzer frontend
const config = {
  // API URL configuration
  apiUrl: process.env.REACT_APP_API_URL || 'http://localhost:8000',
  
  // Environment detection
  isDevelopment: process.env.NODE_ENV === 'development',
  isProduction: process.env.NODE_ENV === 'production',
  
  // Default configuration
  defaultConfig: {
    maxFileSize: 10 * 1024 * 1024, // 10MB
    allowedFileTypes: ['.pdf', '.docx', '.txt'],
  }
};

export default config;
