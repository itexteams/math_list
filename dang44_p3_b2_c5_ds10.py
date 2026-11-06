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


def bt_dang44_p3_b2_c5_ds10(self):
            while True:
                # Random k (chẵn) và m (lẻ)
                # Giới hạn n = k + m thường <= 5 để kết quả < 9999
                k = random.randint(1, 3) # Chọn từ {2, 4, 6, 8}
                m = random.randint(1, 3) # Chọn từ {1, 3, 5, 7, 9}
                n = k + m

                # Tính toán giá trị số tự nhiên
                # Số cách chọn k số chẵn từ 4 số {2,4,6,8}
                chon_chan = math.comb(4, k)
                # Số cách chọn m số lẻ từ 5 số {1,3,5,7,9}
                chon_le = math.comb(5, m)
                # Hoán vị n chữ số
                hoan_vi = math.factorial(n)

                kq_val = hoan_vi * chon_chan * chon_le

                # Kiểm tra điều kiện kết quả < 9999
                if kq_val < 9999:
                    break

            # Đáp án đúng dạng số tự nhiên
            da_dung_str = '$%s$' % latex(kq_val)

            # Tạo các phương án nhiễu (dạng số tự nhiên)
            s_set = set()
            while len(s_set) < 3:
                # Các sai lầm thường gặp: quên hoán vị, sai tổ hợp, hoặc nhầm n
                sai_1 = hoan_vi * math.comb(4, k)
                sai_2 = (hoan_vi // n) * chon_chan * chon_le if n > 1 else kq_val + 10
                offset = random.choice([10, 20, 50, 100, -10, -50])
                nhieu_val = random.choice([sai_1, sai_2, kq_val + offset])

                if nhieu_val > 0 and nhieu_val != kq_val:
                    s_set.add('$%s$' % latex(nhieu_val))

            list_ans = ['\\True ' + da_dung_str] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Có bao nhiêu số tự nhiên có $%s$ chữ số khác nhau và khác $0$ mà trong mỗi số luôn luôn có mặt $%s$ chữ số chẵn và $%s$ chữ số lẻ?'''
                             % (latex(n), latex(k), latex(m)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Số cách chọn $%s$ chữ số chẵn từ tập hợp $\\left\\{2;4;6;8\\right\\}$ là: $C_4^{%s} = %s$ cách. \\\\
                         Số cách chọn $%s$ chữ số lẻ từ tập hợp $\\left\\{1;3;5;7;9\\right\\}$ là: $C_5^{%s} = %s$ cách. \\\\
                         Số cách hoán vị $%s$ chữ số đã chọn để lập thành một số tự nhiên là: $%s! = %s$ cách. \\\\
                         Vậy số các số tự nhiên thỏa mãn yêu cầu bài toán là: $%s \\cdot %s \\cdot %s = %s$ (số).'''
                       % (latex(k), latex(k), latex(chon_chan), 
                          latex(m), latex(m), latex(chon_le), 
                          latex(n), latex(n), latex(hoan_vi),
                          latex(chon_chan), latex(chon_le), latex(hoan_vi), latex(kq_val)))

            # Đáp án ngắn (số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % latex(kq_val)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

