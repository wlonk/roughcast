import fetchMock from 'fetch-mock-jest';

beforeAll(() => {
  window.console.error = jest.fn();
  window.console.warn = jest.fn();
  window.console.info = jest.fn();
  window.api_urls = {
    login: () => '/api/login/',
    logout: () => '/api/logout/',
  };
});

afterEach(fetchMock.reset);
