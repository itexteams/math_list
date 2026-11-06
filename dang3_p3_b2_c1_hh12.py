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


def bt_dang3_p3_b2_c1_hh12(self):
            # Khai báo biến
            # ======= Hàm định dạng số kiểu Việt Nam =======
            def format_vn_decimal(n):
                n = round(float(n), 1)
                if n.is_integer():
                    return str(int(n))
                else:
                    return str(n).replace('.', ',')

            def format_vn_integer(n):
                return str(round(float(n))).replace('.', ',')

            # ======= Tạo điểm A =======
            x0 = random.randint(-5, 3)
            y0 = random.randint(-5, 3)
            z0 = random.randint(0, 5)

            # ======= Sinh vectơ chỉ phương u sao cho z > 0 =======
            while True:
                ux = random.randint(-3, 5)
                uy = random.randint(-3, 5)
                uz = random.randint(1, 5)
                do_dai_u2 = ux**2 + uy**2 + uz**2
                if do_dai_u2 != 0:
                    break

            can_u = sqrt(do_dai_u2)

            # ======= Tốc độ cabin (dưới dạng phân số) =======
            toc_do_raw = round(random.uniform(4.8, 5.2), 1)
            toc_do = Rational(int(toc_do_raw * 10), 10)
            toc_do_display = format_vn_decimal(toc_do)

            # ======= vectơ vận tốc dạng phân số có căn =======
            vx = (toc_do * ux * can_u) / do_dai_u2
            vy = (toc_do * uy * can_u) / do_dai_u2
            vz = (toc_do * uz * can_u) / do_dai_u2

            # ======= Thời gian chuyển động =======
            t = random.randint(5, 40)

            # ======= Tọa độ điểm M dưới dạng biểu thức =======
            xM = x0 + vx * t
            yM = y0 + vy * t
            zM = z0 + vz * t

            # ======= Biểu thức LaTeX =======
            vx_expr = latex(vx)
            vy_expr = latex(vy)
            vz_expr = latex(vz)
            xM_expr = latex(xM)
            yM_expr = latex(yM)
            zM_expr = latex(zM)

            # ======= Hiển thị số kiểu Việt Nam =======
            xM_display = format_vn_integer(xM)
            yM_display = format_vn_integer(yM)
            zM_display = format_vn_integer(zM)

            # ======= Biểu thức tuyến tính =======
            while True:
                a = random.choice([i for i in range(-5, 7) if i not in [0, 1, -1]])
                b = random.choice([i for i in range(-6, 6) if i not in [0, 1, -1]])
                c = random.choice([i for i in range(-4, 8) if i not in [0, 1, -1]])

                if math.gcd(a, b) == 1:
                    break

            ket_qua = a * xM + b * yM + c * zM
            ket_qua_display = format_vn_integer(ket_qua)

            # ======= Chọn kiểu câu hỏi =======
            kieu = random.choice(["do_cao", "bieu_thuc"])

            if kieu == "do_cao":
                noidungcauhoi = (
                    f"Trong không gian $Oxyz$, một cabin cáp treo xuất phát từ điểm $A({x0}; {y0}; {z0})$, chuyển động đều cùng hướng với vectơ "
                    f"$\\vec{{u}}=({ux};{uy}; {uz})$ với tốc độ {toc_do_display} m/s (đơn vị trên mỗi trục tọa độ là mét). "
                    f"Sau {t} giây, cabin cách mặt đất (mặt phẳng $(Oxy)$) bao nhiêu mét? (kết quả làm tròn đến hàng đơn vị)."
                )

                loigiai = f"""Ta có cabin chuyển động đều theo vận tốc $\\vec{{v}}={latex(toc_do)}\\cdot\\frac{{\\vec{{u}}}}{{|\\vec{{u}}|}}=\\left({vx_expr}; {vy_expr}; {vz_expr}\\right)$.
            \\\\
            Vì cabin chuyển động đều cùng hướng với vectơ $\\vec{{u}}$ nên: $\\vec{{AM}} = t \\cdot \\vec{{v}} = {t} \\cdot \\vec{{v}}$.\\\\
            Suy ra: $M = \\left({xM_expr}; {yM_expr}; {zM_expr}\\right)$.\\\\
            Độ cao là $h = {zM_expr} \\approx {format_vn_integer(zM)}$ (m).
            """

                dapan = rf"\shortans[0]{{{format_vn_integer(zM)}}}"

            else:
                noidungcauhoi = (
                    f"Trong không gian $Oxyz$, một cabin xuất phát từ điểm $A({x0}; {y0}; {z0})$, chuyển động đều cùng hướng với vectơ "
                    f"$\\vec{{u}}=({ux}; {uy}; {uz})$ với tốc độ {toc_do_display} m/s (đơn vị trên mỗi trục tọa độ là mét). "
                    f"Sau {t} giây, cabin đến điểm $M(a; b; c)$. Tính giá trị của biểu thức ${a}a+{b}b+{c}c$ (kết quả làm tròn đến hàng đơn vị)."
                )

                loigiai = f"""Ta có cabin chuyển động đều theo vận tốc $\\vec{{v}}={latex(toc_do)}\\cdot\\frac{{\\vec{{u}}}}{{|\\vec{{u}}|}}=\\left({vx_expr}; {vy_expr}; {vz_expr}\\right)$.
            \\\\
            Vì cabin chuyển động đều cùng hướng với vectơ $\\vec{{u}}$ nên: $\\vec{{AM}} = t \\cdot \\vec{{v}} = {t} \\cdot \\vec{{v}}$.\\\\
            Suy ra: $M = \\left({xM_expr}; {yM_expr}; {zM_expr}\\right)$.\\\\
            Khi đó:  
            $ {a}a+{b}b+{c}c = {a}\\cdot\\left({xM_expr}\\right)+{b}\\cdot\\left({yM_expr}\\right)+{c}\\cdot\\left({zM_expr}\\right) \\approx {format_vn_integer(ket_qua)}$.
            """

                dapan = rf"\shortans[0]{{{format_vn_integer(ket_qua)}}}"

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('\\frac', '\\dfrac')
            return content   

