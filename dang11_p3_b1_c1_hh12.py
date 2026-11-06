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


def bt_dang11_p3_b1_c1_hh12(self):
            # Khai báo biến
            def round_SA(a): 
                # Chuyển số về float để xử lý
                val = float(a)
                if val == int(val):
                    return "", str(int(val))

                str_val = f"{val:.5f}".rstrip('0')
                integer_part = str(int(val))
                decimal_part = str_val.split('.')[1] if '.' in str_val else ""

                # Quy tắc làm tròn linh hoạt
                if len(integer_part) >= 3:
                    number = Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    circle = "(làm tròn đến hàng đơn vị)."
                elif len(integer_part) == 2:
                    number = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    circle = "(làm tròn đến hàng phần mười)."
                else:
                    number = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    circle = "(làm tròn đến hàng phần trăm)."

                return circle, str(number).replace('.', ',')

            # ============ XÂY DỰNG BÀI TOÁN ===============================
            # 1. Sinh ngẫu nhiên đối số
            khoi_luong = random.randint(15, 35) # Khối lượng em bé (kg)
            dai_cau_truot = random.randint(25, 50) / 10 # Chiều dài d (m) từ 2.5 đến 5.0
            goc_nghieng = random.randint(5, 9) * 5 # Góc alpha: 25, 30, 35, 40, 45 độ
            g = 9.8

            # 2. Tính toán vật lý
            # Trọng lực P = m.g
            P_val = khoi_luong * g
            # Góc giữa P và d là theta = 90 - alpha
            theta_rad = math.radians(90 - goc_nghieng)
            # Công A = P * d * cos(theta)
            cong_A = float(P_val) * float(dai_cau_truot) * math.cos(theta_rad)

            # 3. Định dạng hiển thị LaTeX
            P_latex = f"{P_val:.1f}".replace('.', '{,}')
            d_latex = f"{dai_cau_truot}".replace('.', '{,}')
            g_latex = "9{,}8"

            # 4. Tinh chỉnh TikZ (Tránh chồng lấn nhãn)
            tikz_code = f"""\\begin{{tikzpicture}}[scale=0.9, font=\\footnotesize, >=stealth]
                    \\coordinate (B) at (0,0);
                    \\coordinate (H) at (5,0);
                    \\coordinate (A) at (5,{{5*tan({goc_nghieng})}});
                    \\draw[thick] (B) -- (H) node[below, pos=0.5] {{Mặt đất}} -- (A) -- cycle;
                    \\draw (4.7,0) -- (4.7,0.3) -- (5,0.3); 
                    \\coordinate (M) at ($(A)!0.3!(B)$);
                    \\draw[red, thick, ->] (M) -- ++(0,-1.2) node[right] {{$\\vec{{P}}$}};
                    \\draw[blue, thick, ->] ($(M)+(-0.2, 0.4)$) -- ($(M)!0.4!(B)+(-0.2, 0.4)$);
                    \\node[blue, above, sloped] at ($(M)!0.2!(B)+(-0.2, 0.4)$) {{$\\vec{{d}}$}};
                    \\path (A) -- (B) node[sloped, pos=0.05, above=6pt] {{$d = {d_latex}$ m}};
                    \\draw (1,0) arc (0:{goc_nghieng}:1);
                    \\node at ({goc_nghieng/2}:1.3) {{${goc_nghieng}^\\circ$}};
                \\end{{tikzpicture}}"""

            de_bai = f"""\\immini{{ Một em nhỏ cân nặng $m = {khoi_luong}$ kg trượt trên cầu trượt dài $d = {d_latex}$ m. 
                    Biết rằng, cầu trượt có góc nghiêng so với phương nằm ngang là ${goc_nghieng}^\\circ$. Lấy gia tốc rơi tự do $g = {g_latex}$ m/s$^2$.
                    }}{{{tikz_code}}}"""

            # 5. Nội dung câu hỏi và lời giải
            hoi = f" Cho biết công $A$ sinh bởi một lực $\\vec{{F}}$ có độ dịch chuyển $\\vec{{d}}$ được tính bởi công thức $A = \\vec{{F}} \\cdot \\vec{{d}}$. Hãy tính công sinh bởi trọng lực $\\vec{{P}}$ khi em nhỏ trượt hết chiều dài cầu trượt. {round_SA(cong_A)[0]} "

            loigiai = f"""Độ lớn của trọng lực tác dụng lên em nhỏ là: \\\\
                    $P = m \\cdot g = {khoi_luong} \\cdot {g_latex} = {P_latex}$ (N). \\\\
                    Vectơ trọng lực $\\vec{{P}}$ hướng thẳng đứng xuống dưới, vectơ dịch chuyển $\\vec{{d}}$ dọc theo mặt cầu trượt. \\\\
                    Góc hợp bởi $\\vec{{P}}$ và $\\vec{{d}}$ là $\\theta = 90^\\circ - {goc_nghieng}^\\circ = {90-goc_nghieng}^\\circ$. \\\\
                    Công sinh bởi trọng lực là: \\\\
                    $A = P \\cdot d \\cdot \\cos \\theta = {P_latex} \\cdot {d_latex} \\cdot \\cos {90-goc_nghieng}^\\circ \\approx {round_SA(cong_A)[1]}$ (J)."""

            # =========== XUẤT CODE LATEX ====================
            # Đáp án (shortans)
            dapan = '\n\\begin{flushright} \\shortans[0]{$%s$} \\end{flushright} \n' % (round_SA(cong_A)[1])

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(de_bai) + str(hoi) + str(dapan) +
                '\\loigiai{ \n'
                + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

