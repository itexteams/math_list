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


def bt_dang28_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                T = random.choice([200, 300, 400, 500])
                # B: Hệ số giảm số lượng công nhân theo thời gian
                B = random.choice([2, 4, 6, 8])
                # A: Số lượng công nhân ban đầu (tính sao cho ngày cuối cùng m(T) = 0 hoặc > 0)
                # Để m(T) = 0 như mẫu, ta chọn A = B * T
                A = B * T

                # P_unit: Đơn giá cho một ngày công (đồng)
                P_unit = random.choice([300000, 400000, 450000, 500000, 600000])
                P_unit_str = "{:,}".format(P_unit).replace(',', '.') # Định dạng phân cách nghìn bằng dấu chấm

                total_man_days = int(A * T - (B / 2) * (T**2))

                # Tổng chi phí (VND)
                total_cost_vnd = total_man_days * P_unit
                # Đổi sang tỷ VNĐ
                total_cost_billion = Decimal(total_cost_vnd) / Decimal(10**9)

                # Định dạng đáp án đúng
                if total_cost_billion == int(total_cost_billion):
                    kq_str = str(int(total_cost_billion))
                else:
                    kq_str = str(total_cost_billion).replace('.', ',')

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                da_dung = '$%s$' % kq_str

                s = set()
                while len(s) < 3:
                    # Tạo sai số dựa trên giá trị tỷ
                    offset = random.choice([5, 10, 15, -5, -10, 2, 4])
                    sai_val = float(total_cost_billion) + offset
                    if sai_val > 0:
                        sai_str = '$%s$' % str(round(sai_val, 1)).replace('.', ',')
                        if sai_str != da_dung:
                            s.add(sai_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # B2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = (r'''Đối với các dự án xây dựng, chi phí nhân công lao động được tính theo số ngày công. Gọi $m(t)$ là số lượng công nhân được sử dụng ở ngày thứ $t$ (kể từ khi khởi công dự án). Gọi $M(t)$ là số ngày công được tính đến hết ngày thứ $t$ (kể từ khi khởi công dự án). Trong kinh tế xây dựng, người ta đã biết rằng $M'(t) = m(t)$. Một công trình xây dựng dự kiến hoàn thành trong $%s$ ngày. Số lượng công nhân được sử dụng cho bởi hàm số $m(t) = %s - %st$, trong đó $t$ tính theo ngày ($0 \le t \le %s$), $m(t)$ tính theo người. Đơn giá cho một ngày công lao động là $%s$ đồng. Chi phí (đơn vị: Tỷ VNĐ) nhân công lao động của công trình đó đến lúc hoàn thành bằng bao nhiêu?'''
                                 % (latex(T), latex(A), latex(B), latex(T), P_unit_str))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_ans = [da_d, das1, das2, das3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                # Hệ số B/2 trong latex
                hiso_M = Rational(B, 2)

                loigiai = (r'''$\int m(t) \text{d}t = \int (%s - %st) \text{d} t = %st - %st^2 + C$. \\
                             Tại $t = 0$ thì $M(t) = 0 \Leftrightarrow C = 0$. \\
                             Vậy $M(t) = %st - %st^2$. \\
                             Số ngày công tính đến khi hoàn thành dự án là: $M(%s) = %s \cdot %s - %s \cdot %s^2 = %s$ (ngày). \\
                             Chi phí nhân công lao động của công trình đó là: $%s \cdot %s = %s$ đồng $= %s$ tỷ VNĐ.'''
                           % (latex(A), latex(B), latex(A), latex(hiso_M),
                              latex(A), latex(hiso_M),
                              latex(T), latex(A), latex(T), latex(hiso_M), latex(T), latex(total_man_days),
                              latex(total_man_days), P_unit_str, "{:,}".format(total_cost_vnd).replace(',', '.'), kq_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

