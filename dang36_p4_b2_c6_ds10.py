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


def bt_dang36_p4_b2_c6_ds10(self):
            #Khai báo biến
            # m: Số cặp vợ chồng (Trong ảnh là 4)
            n = random.randint(8, 12)
            m = random.randint(3, 6)
            tong_nguoi = 2 * n

            # B2: Tính toán chi tiết theo logic bài toán
            # 1. Số phần tử không gian mẫu
            n_omega = binomial(tong_nguoi, 3)

            # 2. Tính biến cố đối A_bar: "3 người được chọn có 1 cặp vợ chồng"
            # - Chọn 1 cặp vợ chồng từ m cặp: C(m, 1)
            # - Chọn 1 người còn lại từ (tong_nguoi - 2) người: C(tong_nguoi - 2, 1)
            n_A_bar = binomial(m, 1) * binomial(tong_nguoi - 2, 1)

            # 3. Số phần tử của biến cố A: "Không có cặp vợ chồng nào"
            n_A = n_omega - n_A_bar

            # 4. Xác suất
            xac_suat = Rational(n_A, n_omega)
            phan_so_latex = latex(xac_suat)

            # B4: Điều chỉnh các phương án sai
            # Tạo danh sách các phương án sai ngẫu nhiên quanh đáp án đúng
            list_wrong = []
            while len(list_wrong) < 3:
                # Tạo các tử số khác nhau để tạo phương án nhiễu
                sai_tu = n_A + random.choice([-20, -10, 10, 20, 45, -5])
                if sai_tu > 0 and sai_tu != n_A:
                    ps_sai = Rational(sai_tu, n_omega)
                    ps_sai_latex = '$%s$' % (latex(ps_sai))
                    if ps_sai_latex not in list_wrong and ps_sai != xac_suat:
                        list_wrong.append(ps_sai_latex)

            # Đáp án đúng
            da_dung = '\\True $%s$' % (phan_so_latex)

            # Trộn đáp án
            list_all_choices = [da_dung] + list_wrong
            random.shuffle(list_all_choices)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong một buổi liên hoan có $%s$ cặp nam nữ. Trong đó có $%s$ cặp vợ chồng. Chọn ngẫu nhiên 3 người để biểu diễn một tiết mục văn nghệ. Tính xác suất để 3 người được chọn không có cặp vợ chồng nào.'''
                             % (latex(n), latex(m)))

            # Nội dung lời giải chi tiết (không viết tắt, trình bày như ảnh)
            loigiai = ('''Tổng số người trong buổi liên hoan là $%s \\cdot 2 = %s$ người. \\\\
            Số phần tử của không gian mẫu là $n\\left( \\Omega \\right) = C_{%s}^{3} = %s$. \\\\
            Gọi $A$ là biến cố: "3 người được chọn không có cặp vợ chồng nào". \\\\
            Khi đó biến cố đối $\\overline{A}$ là: "3 người được chọn có 1 cặp vợ chồng". \\\\
            - Chọn một cặp vợ chồng trong $%s$ cặp có $C_{%s}^{1}$ cách. \\\\
            - Chọn thêm 1 người trong $%s - 2 = %s$ người còn lại có $C_{%s}^{1}$ cách. \\\\
            Suy ra số phần tử của biến cố $\\overline{A}$ là $n\\left( \\overline{A} \\right) = C_{%s}^{1} \\cdot C_{%s}^{1} = %s \\cdot %s = %s$. \\\\
            Suy ra số phần tử của biến cố $A$ là $n\\left( A \\right) = %s - %s = %s$. \\\\
            Vậy xác suất cần tính là $P\\left( A \\right) = \\frac{%s}{%s} = %s$.'''
                       % (latex(n), latex(tong_nguoi), 
                          latex(tong_nguoi), latex(n_omega),
                          latex(m), latex(m),
                          latex(tong_nguoi), latex(tong_nguoi - 2), latex(tong_nguoi - 2),
                          latex(m), latex(tong_nguoi - 2), latex(m), latex(tong_nguoi - 2), latex(n_A_bar),
                          latex(n_omega), latex(n_A_bar), latex(n_A),
                          latex(n_A), latex(n_omega), phan_so_latex))

            # Xuất kết quả theo định dạng yêu cầu (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

