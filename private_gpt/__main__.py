# start a fastapi server with uvicorn

import uvicorn

from private_gpt.main import app
from private_gpt.settings.settings import settings

# Set log_config=None to do not use the uvicorn logging configuration, and
# use ours instead. For reference, see below:
# https://github.com/tiangolo/fastapi/discussions/7457#discussioncomment-5141108
# uvicorn.run(app, port=settings().server.port, log_config=None)
_blocks = app.get_ui_blocks()
_blocks.queue()
_blocks.launch(share=True, debug=False, show_api=False)
