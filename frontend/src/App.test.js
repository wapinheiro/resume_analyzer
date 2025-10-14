import { render, screen } from '@testing-library/react';
import App from './App';

test('renders resume analyzer heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/resume analyzer/i);
  expect(headingElement).toBeInTheDocument();
});
