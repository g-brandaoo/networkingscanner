# # Network Scanner (Python)

Scanner de rede local desenvolvido em Python com suporte a múltiplas portas, concorrência e banner grabbing básico.

## Objetivo

Projeto educacional focado em:
- entendimento prático de redes (IP, portas)
- uso de sockets (baixo nível)
- concorrência com threads
- fundamentos de port scanning

## Funcionalidades

- Varredura de IPs em rede local (/24)
- Scan de múltiplas portas TCP
- Detecção de portas abertas
- Identificação básica de serviços (banner grabbing)
- Execução concorrente para maior velocidade
- Listagem de hosts ativos

## Tecnologias

- Python 3
- socket
- concurrent.futures (ThreadPoolExecutor)

## Configuração

Edite os parâmetros no topo do código:

```python
BASE_IP = "192.168.0"
PORTS = [21, 22, 23, 53, 80, 443, 8080, 7547]
TIMEOUT = 1
MAX_THREADS = 100

 Como usar
Descubra seu IP local (ex: 192.168.1.23)
Ajuste o BASE_IP conforme sua rede (ex: 192.168.1)
Execute: python main.py
Exemplo de saída
[OPEN] 192.168.0.1:80 -> b'HTTP/1.1 200 OK...'
[OPEN] 192.168.0.1:443 -> b''

Scan finalizado.

Hosts ativos encontrados:
192.168.0.1

Como funciona

O script:

Gera IPs no range definido (1–254)
Testa conexões TCP em múltiplas portas
Identifica portas abertas
Tenta capturar resposta do serviço (banner)
Limitações
Não detecta dispositivos sem portas abertas
Pode gerar falsos negativos (timeout/rede)
Não realiza scan completo de portas
Não utiliza ICMP (ping)
Não é stealth
Não substitui ferramentas profissionais como Nmap
Aviso legal

Este projeto é exclusivamente educacional.
Não utilize em redes sem autorização.

Próximas melhorias
Detecção de hosts via ICMP (ping)
Scan completo de portas (range 1–65535)
Exportação de resultados (JSON/CSV)
Interface CLI com argumentos (argparse)
Identificação de serviços mais precisa

Autor

Projeto desenvolvido para estudo prático de redes e cibersegurança.
