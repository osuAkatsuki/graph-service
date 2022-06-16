import uvicorn
import logging

import app.state

__author__ = "lenforiee"
__email__ = "lenforiee@gmail.com"
__discord__ = "lenforiee#0088"


def main() -> int:

    uvicorn.run(
        "app.api.init_api:asgi_app",
        uds=app.state.config.SOCKET_FILE,
        log_level=logging.WARNING,
        server_header=False,
        reload=app.state.config.DEBUG,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
