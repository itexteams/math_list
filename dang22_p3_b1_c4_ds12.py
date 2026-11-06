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


def bt_dang22_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo danh sách các dạng biến thể để random
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            if dang == '1':
                # Biến thể 1: Giống hệt ảnh (Mặt 1 chấm và mặt lẻ)
                val_a = 1
                ten_b = "lẻ"
                tap_b = [1, 3, 5]
                loigiai_b = "B = \\{1; 3; 5\\}"
            elif dang == '2':
                # Biến thể 2: Mặt 2 chấm và mặt chẵn
                val_a = 2
                ten_b = "chẵn"
                tap_b = [2, 4, 6]
                loigiai_b = "B = \\{2; 4; 6\\}"
            else:
                # Biến thể 3: Mặt 5 chấm và mặt lớn hơn hoặc bằng 3
                val_a = 5
                ten_b = "lớn hơn hoặc bằng 3"
                tap_b = [3, 4, 5, 6]
                loigiai_b = "B = \\{3; 4; 5; 6\\}"

            # Tính toán xác suất
            n_omega = 6
            n_B = len(tap_b)
            p_B = Rational(n_B, n_omega)
            p_AB = Rational(1, n_omega) # Vì val_a luôn nằm trong tap_b ở các ví dụ trên
            p_cond = p_AB / p_B

            # Định dạng số thập phân làm tròn đến hàng phần trăm, dùng dấu phẩy
            kq_float = float(p_cond)
            kq_dec = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_dec).replace('.', ',')

            # Tạo các phương án sai (không trùng đáp án đúng)
            sai_1 = str(Decimal(str(kq_float + 0.15)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
            sai_2 = str(Decimal(str(abs(kq_float - 0.12))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
            sai_3 = str(Decimal(str(kq_float + 0.24)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

            # Đảm bảo phương án sai không vô tình trùng phương án đúng
            while sai_1 == kq_str or sai_1 == sai_2 or sai_1 == sai_3:
                sai_1 = str(round(random.uniform(0.1, 0.9), 2)).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Gieo một con xúc xắc cân đối và đồng chất một lần. Gọi $A$ là biến cố xuất hiện mặt $%s$ chấm, $B$ là biến cố xuất hiện mặt %s chấm. Tính xác suất có điều kiện $P(A|B)$? (Kết quả làm tròn đến hàng phần trăm).'''
                             % (latex(val_a), ten_b))

            # Các đáp án
            da_d = ('\\True ' + kq_str)
            list_1 = [da_d, sai_1, sai_2, sai_3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = ('''Không gian mẫu khi gieo xúc xắc là $\\Omega = \\{1; 2; 3; 4; 5; 6\\} \\Rightarrow n(\\Omega) = 6$. \\\\
                      Biến cố $B$ xuất hiện mặt %s chấm nên $%s \\Rightarrow n(B) = %s$. \\\\
                      Xác suất của biến cố $B$ là $P(B) = \\frac{%s}{6} = %s$. \\\\
                      Biến cố $AB$ là biến cố mặt xuất hiện vừa là mặt $%s$ chấm, vừa là mặt %s chấm. \\\\
                      Vì $%s \\in B$ nên $AB = \\{%s\\} \\Rightarrow n(AB) = 1$. \\\\
                      Xác suất biến cố giao là $P(AB) = \\frac{1}{6}$. \\\\
                      Xác suất có điều kiện cần tìm là: \\\\
                      $P(A|B) = \\frac{P(AB)}{P(B)} = \\frac{1/6}{%s/6} = \\frac{1}{%s} \\approx %s$.'''
                       % (ten_b, loigiai_b, latex(n_B), latex(n_B), latex(p_B), 
                          latex(val_a), ten_b, latex(val_a), latex(val_a), latex(n_B), latex(n_B), kq_str))
            dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

