from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

hostName = "localhost"
serverPort = 8080

ROOT_PATH = Path(__file__).parent
HH_PATH = Path.joinpath(ROOT_PATH, "index.html")


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def __get_html_content(self):
        with open(HH_PATH, 'r', encoding='utf-8') as f:
            data = f.read()
        return data

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        # query_components = parse
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
