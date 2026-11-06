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


def bt_dang60_p3_b2_c5_ds10(self):
            while True:
                # Giới hạn số lượng câu hỏi để tổng tổ hợp < 9999
                # nk (khó): 2-4, ntb (trung bình): 3-6, nd (dễ): 4-8
                nk = randint(2, 4)
                ntb = randint(3, 6)
                nd = randint(4, 8)
                tong_cau = nk + ntb + nd

                # Tính toán các trường hợp (Sử dụng math.comb để ra số tự nhiên)
                # TH1: 2 dễ, 2 trung bình, 1 khó
                kq_th1 = math.comb(nd, 2) * math.comb(ntb, 2) * math.comb(nk, 1)

                # TH2: 2 dễ, 1 trung bình, 2 khó
                kq_th2 = math.comb(nd, 2) * math.comb(ntb, 1) * math.comb(nk, 2)

                # TH3: 3 dễ, 1 trung bình, 1 khó
                kq_th3 = math.comb(nd, 3) * math.comb(ntb, 1) * math.comb(nk, 1)

                # Tổng kết quả
                kq_cuoi = kq_th1 + kq_th2 + kq_th3

                # Kiểm tra điều kiện đề bài yêu cầu kq < 9999
                if 0 < kq_cuoi < 9999:
                    break

            # Đáp án đúng dạng số tự nhiên
            da_dung_str = '$%s$' % latex(kq_cuoi)

            # Tạo các phương án sai (nhiễu số học)
            s_set = set()
            while len(s_set) < 3:
                # Các sai lầm thường gặp: cộng các tổ hợp, hoặc sai lệch đơn vị
                offset = random.choice([10, 50, 100, -10, -50, 200, -100])
                nhieu_val = random.choice([kq_th1 + kq_th2, kq_cuoi + offset, (nd+ntb+nk)*5])

                if nhieu_val > 0 and nhieu_val != kq_cuoi:
                    s_set.add('$%s$' % latex(nhieu_val))

            list_ans = ['\\True ' + da_dung_str] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Thầy A có $%s$ câu hỏi khác nhau gồm $%s$ câu khó, $%s$ câu trung bình và $%s$ câu dễ. Từ $%s$ câu hỏi đó có thể lập được bao nhiêu đề kiểm tra, mỗi đề gồm $5$ câu hỏi khác nhau, sao cho trong mỗi đề nhất thiết phải có đủ cả $3$ loại câu và số câu dễ không ít hơn $2$?'''
                             %(latex(tong_cau), latex(nk), latex(ntb), latex(nd), latex(tong_cau)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Để lập đề kiểm tra gồm $5$ câu hỏi có đủ $3$ loại và số câu dễ không ít hơn $2$, ta có các trường hợp sau: \\\\
                         - TH1: Đề gồm $2$ câu dễ, $2$ câu trung bình và $1$ câu khó: $C_{%s}^{2} \\cdot C_{%s}^{2} \\cdot C_{%s}^{1} = %s$ (đề). \\\\
                         - TH2: Đề gồm $2$ câu dễ, $1$ câu trung bình và $2$ câu khó: $C_{%s}^{2} \\cdot C_{%s}^{1} \\cdot C_{%s}^{2} = %s$ (đề). \\\\
                         - TH3: Đề gồm $3$ câu dễ, $1$ câu trung bình và $1$ câu khó: $C_{%s}^{3} \\cdot C_{%s}^{1} \\cdot C_{%s}^{1} = %s$ (đề). \\\\
                         Vậy tổng số đề kiểm tra có thể lập được là: $%s + %s + %s = %s$ (đề).'''
                       %(latex(nd), latex(ntb), latex(nk), latex(kq_th1),
                         latex(nd), latex(ntb), latex(nk), latex(kq_th2),
                         latex(nd), latex(ntb), latex(nk), latex(kq_th3),
                         latex(kq_th1), latex(kq_th2), latex(kq_th3), latex(kq_cuoi)))

            # Đáp án ngắn (Cập nhật kết quả số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_cuoi))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

