from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os

PORTA = 8000
ARQUIVO = "senha_teste.txt"

class Servidor(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/status":
            self.enviar_json({
                "online": True
            })
            return

        super().do_GET()

    def do_POST(self):
        if self.path != "/salvar":
            self.send_error(404)
            return

        tamanho = int(self.headers.get("Content-Length", 0))
        dados = self.rfile.read(tamanho)

        try:
            recebido = json.loads(dados)
            senha = recebido.get("senha", "")

            if not senha or len(senha) > 6:
                self.enviar_json({
                    "ok": False
                })
                return

            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                arquivo.write(senha)

            self.enviar_json({
                "ok": True
            })

        except:
            self.enviar_json({
                "ok": False
            })

    def enviar_json(self, dados):
        resposta = json.dumps(dados).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(resposta)))
        self.end_headers()

        self.wfile.write(resposta)

print("================================")
print("       PASSWORD LAB V2")
print("================================")
print()
print("Servidor: http://localhost:8000")
print()
print("Abra esse endereço no navegador.")
print("CTRL+C para parar.")
print()

servidor = HTTPServer(("localhost", PORTA), Servidor)
servidor.serve_forever()