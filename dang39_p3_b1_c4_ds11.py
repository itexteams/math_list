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


def bt_dang39_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random độ cao h (số nguyên từ 5 đến 20 mét)
                h = randint(5, 20)

                # Random tỉ lệ nảy q (chọn các tỉ lệ để ra số đẹp)
                cac_ti_le = [(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (3, 5), (4, 5)]
                tu_so, mau_so = random.choice(cac_ti_le)
                q = Rational(tu_so, mau_so)

                # --- Tính toán kết quả ---
                # Tổng quãng đường S = h + 2*h*q / (1-q)
                phan_nay_sau = 2 * h * q / (1 - q)
                ket_qua = h + phan_nay_sau

                # Format kết quả
                kq = latex(ket_qua)

                # --- Tạo các đáp án nhiễu ---
                sai_1 = h + h * q / (1 - q) # Quên nhân 2
                sai_2 = h / (1 - q)         # Cấp số nhân lùi đơn thuần
                sai_3 = ket_qua + randint(1, 5)
                if sai_3 == ket_qua: sai_3 = ket_qua + 10

                du = ['$%s$' % kq]
                da = du[0] 

                s = [
                    '$%s$' % latex(sai_1),
                    '$%s$' % latex(sai_2),
                    '$%s$' % latex(sai_3),
                    '$%s$' % latex(ket_qua + 2),
                    '$%s$' % latex(ket_qua - 2)
                ]

                ds_sai = random.sample(s, 3)
                da_s1 = ds_sai[0]
                da_s2 = ds_sai[1]
                da_s3 = ds_sai[2]

                # --- Chuẩn bị text hiển thị ---
                text_h = latex(h)
                text_q = latex(q)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong một lần Đoàn trường tổ chức chơi bóng chuyền hơi, bạn Nam thả một quả bóng chuyền hơi từ tầng ba, độ cao $%s m$ so với mặt đất và thấy rằng mỗi lần chạm đất thì quả bóng lại nảy lên một độ cao bằng $%s$ độ cao lần rơi trước. Biết quả bóng chuyển động vuông góc với mặt đất. Khi đó tổng quãng đường (đơn vị: m) quả bóng đã bay từ lúc thả bóng đến khi quả bóng đứng im bằng bao nhiêu'''
                                 % (text_h, text_q))

                # --- Tính toán hiển thị lời giải ---
                # u1 của phần đuôi = 2 * h * q
                u1_duoi = 2 * h * q
                # Tổng phần đuôi
                tong_duoi = u1_duoi / (1 - q)

                # Lời giải đã sửa ( và ) thành \left( và \right)
                # Lưu ý: Trong chuỗi Python, backslash phải viết là \\
                loigiai = ('''Lần đầu rơi xuống, quãng đường quả bóng đã bay đến lúc chạm đất là $%s m$. \\\\
                Sau đó quả bóng nảy lên và rơi xuống chạm đất lần thứ 2 thì quãng đường quả bóng đã bay là $%s + 2 \\cdot %s \\cdot %s$. \\\\
                Tương tự, khi quả bóng nảy lên và rơi xuống chạm đất lần thứ $n$ thì quãng đường quả bóng đã bay là:
                $$ S_n = %s + 2 \\cdot %s \\cdot %s + \\dots + 2 \\cdot %s \\cdot \\left(%s\\right)^{n-1} $$
                $$ = %s + \\frac{2 \\cdot %s \\cdot %s \\cdot \\left(1 - \\left(%s\\right)^{n-1}\\right)}{1 - %s} = %s + %s \\left(1 - \\left(%s\\right)^{n-1}\\right) $$
                Quãng đường quả bóng đã bay từ lúc thả đến lúc không nảy nữa bằng:
                $$ \\lim_{n \\to +\\infty} \\left[%s + %s \\left(1 - \\left(%s\\right)^{n-1}\\right)\\right] = %s + %s = %s \\text{m.}$$'''
                % (
                    text_h,                                         # 8m
                    text_h, text_h, text_q,                         # 8 + 2.8.3/4
                    text_h, text_h, text_q, text_h, text_q,         # Sn dòng 1
                    text_h, text_h, text_q, text_q, text_q,         # Sn dòng 2 (phần phân số)
                    text_h, latex(tong_duoi), text_q,               # Sn dòng 2 (phần rút gọn)
                    text_h, latex(tong_duoi), text_q,               # Biểu thức lim
                    text_h, latex(tong_duoi), kq                    # Kết quả cuối
                ))

                # Shuffle đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(da_s1), str(da_s2), str(da_s3)]
                random.shuffle(list_1)

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

