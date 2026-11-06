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


def bt_dang18_p4_b3_c4_ds11(self):
            # Khai báo biến
            def generate_question():
                x, m = symbols('x m')

                # 1. Tạo điểm x0 và phần tử căn thức sao cho số đẹp
                x0 = random.randint(1, 5)
                # Chọn c sao cho x0 + c = k^2
                k = random.randint(2, 4)
                c = k**2 - x0
                mau_so = sqrt(x + c) - k

                # 2. Tạo tử số (x-x0)(x-b)
                b = random.randint(-2, 5)
                tu_so = (x - x0) * (x - b)
                f_tren = tu_so / mau_so

                # 3. Tính giới hạn phải (Số L)
                L = limit(f_tren, x, x0, dir='+')

                # 4. Tạo hàm bậc 2 theo m: A*m^2*x + B*m + C
                # Để đơn giản và hay gặp, ta tạo dạng sao cho phương trình có nghiệm đẹp
                A = random.choice([1, 2])
                target_m = random.randint(-2, 2)
                # Giả sử ta muốn phương trình (m - target_m)^2 = 0 tại x0
                # f_duoi = A*x*m^2 + B*m + C
                # Ở đây tôi random các hệ số để phương trình có thể có 0, 1 hoặc 2 nghiệm
                coeff_B = random.randint(-10, 10)
                coeff_C = random.randint(-10, 10)
                f_duoi = A * m**2 * x + coeff_B * m + coeff_C

                # 5. Giải tìm m
                f_x0 = f_duoi.subs(x, x0)
                phuong_trinh = f_x0 - L
                ds_m = solve(phuong_trinh, m)
                so_luong_m = len(ds_m)

                # --- XỬ LÝ ĐÁP ÁN ---
                da_dung = f"{so_luong_m}"
                options = ["0", "1", "2", "3"] # Các lựa chọn phổ biến cho câu hỏi "Có bao nhiêu"
                if da_dung not in options: options.append(da_dung)

                choices = ["\\True " + da_dung]
                others = [opt for opt in options if opt != da_dung]
                random.shuffle(others)
                choices += others[:3]
                random.shuffle(choices)

                # --- NỘI DUNG ---
                noidungcauhoi = (r"Cho hàm số $f(x) = \begin{cases} \frac{%s}{%s} & \text{khi } x > %s \\ %s & \text{khi } x \le %s \end{cases}$, $m$ là tham số. Tìm số giá trị của $m$ để hàm số đã cho liên tục tại $x = %s$." 
                                 % (latex(expand(tu_so)), latex(mau_so), x0, latex(f_duoi), x0, x0))

                loigiai = (r"Ta có:\\"
                           r"$\lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} \frac{%s}{%s} = %s$.\\"
                           r"$\lim_{x \to %s^-} f(x) = f(%s) = %s$.\\"
                           r"Để hàm số liên tục tại $x = %s$ thì $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^-} f(x)$.\\"
                           r"$\Leftrightarrow %s = %s \Leftrightarrow %s = 0$.\\"
                           % (x0, x0, latex(expand(tu_so)), latex(mau_so), L, x0, x0, latex(f_x0), x0, x0, x0, latex(f_x0), L, latex(simplify(phuong_trinh))))

                if so_luong_m == 0:
                    loigiai += "Phương trình vô nghiệm $m$. Vậy không có giá trị $m$ nào thỏa mãn."
                else:
                    loigiai += r"Giải phương trình ta được $m \in \{ %s \}$. Vậy có %s giá trị $m$ thỏa mãn." % (", ".join([latex(sol) for sol in ds_m]), so_luong_m)

                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
                return content
            content = generate_question()
            return content 

