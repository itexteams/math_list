import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang26_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3 - Logic Random bài toán: 
                # Lặp để chọn ngẫu nhiên 3 cạnh tạo thành một tam giác hợp lệ
                while True:
                    AB = round(random.uniform(3.0, 8.0), 1)
                    BC = round(random.uniform(3.0, 8.0), 1)
                    CA = round(random.uniform(3.0, 8.0), 1)
                    # Điều kiện để 3 cạnh tạo thành tam giác (có cộng thêm 0.5 để tránh tam giác quá dẹt)
                    if AB + BC > CA + 0.5 and BC + CA > AB + 0.5 and CA + AB > BC + 0.5:
                        break

                # Chuyển số thập phân sang dạng chuỗi có dấu phẩy kiểu Việt Nam
                AB_str = str(AB).replace('.', ',')
                BC_str = str(BC).replace('.', ',')
                CA_str = str(CA).replace('.', ',')

                # Tính nửa chu vi p
                p_val = (AB + BC + CA) / 2.0

                # Xử lý hiển thị p dưới dạng phân số tối giản (giống 31/4 trong bài mẫu)
                tu_so = int(round((AB + BC + CA) * 10))
                mau_so = 20
                ucln = math.gcd(tu_so, mau_so)
                tu_so = tu_so // ucln
                mau_so = mau_so // ucln
                if mau_so == 1:
                    p_str = f"{tu_so}"
                else:
                    p_str = f"\\frac{{{tu_so}}}{{{mau_so}}}"

                # Tính S bằng công thức Heron và tính R
                S_val = math.sqrt(p_val * (p_val - AB) * (p_val - BC) * (p_val - CA))
                R_val = (AB * BC * CA) / (4 * S_val)

                # Làm tròn giống bài mẫu
                S_round = round(S_val, 1)
                R_round = round(R_val, 2)

                # Đổi dấu chấm thành phẩy
                S_str = str(S_round).replace('.', ',')
                R_str = str(R_round).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Trong khi khai quật một ngôi mộ cổ, các nhà khảo cổ học đã tìm được một chiếc đĩa cổ hình tròn bị vỡ, các nhà khảo cổ muốn khôi phục lại hình dạng chiếc đĩa này. Để xác định bán kính của chiếc đĩa, các nhà khảo cổ lấy $3$ điểm trên chiếc đĩa và tiến hành đo đạc thu được kết quả như hình vẽ ($AB = %s \\text{ cm}; BC = %s \\text{ cm}; CA = %s \\text{ cm}$). Bán kính chiếc đĩa (Kết quả làm tròn đến hàng phần trăm) bằng}
                {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
