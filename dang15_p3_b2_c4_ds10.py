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


def bt_dang15_p3_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Giả sử đỉnh I có tọa độ (x0, y0). Ta chọn x0 trước để bài toán đẹp.
                x0 = randint(-5, 5)
                # Tránh trường hợp m = 0 theo điều kiện đề bài
                m_val = 0
                while m_val == 0:
                    m_val = randint(-10, 10)

                # Từ công thức x0 = -b/(2a). Với y = mx^2 + bx + c.
                # Ta chọn b sao cho -b/(2m) = x0 => b = -2*m*x0
                b_coeff = -2 * m_val * x0

                # Chọn ngẫu nhiên một giá trị c ban đầu dưới dạng tham số m: y = mx^2 + bx + (km + n)
                k = randint(-5, 5)
                n = randint(-5, 5)
                # Phương trình parabol: y = m*x^2 + b_coeff*x + (k*m + n)
                # Tại đỉnh x = x0: y0 = m(x0)^2 + (-2*m*x0)*x0 + km + n = m(x0^2 - 2x0^2 + k) + n
                # y0 = m(k - x0^2) + n

                # Chọn đường thẳng y = Ax + B sao cho m giải ra số nguyên hoặc phân số đẹp
                # Ở đây ta giả lập lại giống ảnh: y = 3x - 1
                A = randint(1, 5)
                B = randint(-5, 5)

                # Phương trình tìm m: y0 = A*x0 + B
                # m(k - x0^2) + n = A*x0 + B
                # m = (A*x0 + B - n) / (k - x0^2)

                # Để đảm bảo m ra số cụ thể như đề bài, ta sẽ cố định m trước rồi suy ngược lại n
                target_m = randint(-5, 5)
                if target_m == 0: target_m = 1

                # Tính toán n để m đúng bằng target_m
                # n = A*x0 + B - target_m * (k - x0^2)
                n = A*x0 + B - target_m * (k - x0**2)

                # Biểu thức y theo m: y = m*x^2 + (b_coeff/m)*m*x + (k*m + n)
                # Để giống ảnh: y = mx^2 - 2mx - 3m - 2 (m # 0)
                # Ta có: b = -2*x0*m, c = k*m + n

                # Các giá trị hiển thị trong đề bài
                hso_b_theo_m = -2 * x0
                hso_c_m = k
                hso_c_so = n

                # Tọa độ đỉnh I thực tế
                y_dinh_bieuthuc = target_m * (k - x0**2) + n

                # Đáp án đúng
                da_dung = target_m

                # B4: Tạo các phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = target_m + randint(-4, 4)
                    if sai != target_m and sai != 0:
                        s.add(sai)
                list_sai = list(s)

                # Câu hỏi
                # Biểu diễn c = k*m + n
                c_str = ""
                if hso_c_m != 0:
                    c_str += f"{hso_c_m}m"
                if hso_c_so > 0:
                    c_str += f"+{hso_c_so}"
                elif hso_c_so < 0:
                    c_str += f"{hso_c_so}"

                noidungcauhoi = (r"Cho hàm số $y = mx^2 %sm %s$ ($m \neq 0$). Giá trị của $m$ để đồ thị hàm số có đỉnh thuộc đường thẳng $y = %sx %s$ bằng bao nhiêu?"
                                 %(latex(hso_b_theo_m) + "x", c_str, latex(A), latex(B) if B < 0 else "+"+str(B)))

                # Các đáp án
                da_d = ('\\True $%s$' % (latex(da_dung)))
                da_s1 = '$%s$' % (latex(list_sai[0]))
                da_s2 = '$%s$' % (latex(list_sai[1]))
                da_s3 = '$%s$' % (latex(list_sai[2]))

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Nội dung lời giải chi tiết theo mẫu ảnh
                loigiai=(r"Ta có $x = -\frac{b}{2a} = \frac{%sm}{2m} = %s$, suy ra $y = m(%s)^2 %sm(%s) %s = %sm %s$. \\" "\n"
                         r"Do đó tọa độ đỉnh $I(%s; %sm %s)$.\\" "\n"
                         r"Theo giả thiết đỉnh $I$ thuộc đường thẳng $y = %sx %s$ nên ta có:\\" "\n"
                         r"$ %sm %s = %s \cdot %s %s \Leftrightarrow %sm = %s \Leftrightarrow m = %s $.\\" "\n"
                         r"Vậy $m = %s$ thỏa mãn yêu cầu bài toán."
                         %(latex(-hso_b_theo_m), latex(x0), latex(x0), latex(hso_b_theo_m), latex(x0), c_str, latex(k - x0**2), latex(n),
                           latex(x0), latex(k - x0**2), latex(n), latex(A), latex(B) if B < 0 else "+"+str(B),
                           latex(k - x0**2), latex(n), latex(A), latex(x0), latex(B) if B < 0 else "+"+str(B),
                           latex(k - x0**2), latex(A*x0 + B - n), latex(target_m), latex(target_m)
                         ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(target_m))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

