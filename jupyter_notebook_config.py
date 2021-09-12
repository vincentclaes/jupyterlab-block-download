import sys
from pathlib import Path
sys.path.append(str(Path(Path.home(),".jupyter")))
import handlers
c.ContentsManager.files_handler_class = 'handlers.ForbidFilesHandler'
c.ContentsManager.files_handler_params = {}
