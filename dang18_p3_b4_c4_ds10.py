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


def bt_dang18_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Khởi tạo danh sách dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random bộ số Pitago (k*3, k*4, k*5) để AM là số nguyên
                # AB = 6k, BM = 8k -> AM = 10k
                k = randint(1, 3)
                ab = 6 * k
                bm_val = 8 * k
                am_val = 10 * k

                # Vận tốc: v1 (tàu) và v2 (xe máy)
                v1 = 10 * k
                v2 = 30 * k

                # Khoảng cách BC = BM + MC. Chọn MC sao cho thời gian MC/v2 hữu tỉ đẹp
                # Chọn MC = d * k. Giả sử d=7 như trong bài gốc.
                d = randint(5, 12)
                mc_val = d * k
                bc = bm_val + mc_val

                # Tính toán thời gian T
                # T = AM/v1 + MC/v2 = 10k/10k + dk/30k = 1 + d/30 (giờ)
                t_hour_frac = Rational(30 + d, 30)
                total_minutes = int(float(t_hour_frac) * 60)
                h = total_minutes // 60
                m = total_minutes % 60
                time_str = f"{h}h{m} phút"

                # Tính tổng quãng đường S = AM + MC
                s_val = am_val + mc_val

                # Đáp án đúng
                da = f"${s_val}$ km"

                # Các đáp án nhiễu
                s_nhieu = set()
                while len(s_nhieu) < 3:
                    fake = s_val + random.choice([-3, -2, -1, 1, 2, 3, 5])
                    if fake > 0 and fake != s_val:
                        s_nhieu.add(fake)

                list_nhieu = [f"${x}$ km" for x in s_nhieu]
                das1, das2, das3 = list_nhieu

                # Câu hỏi
                noidungcauhoi = ('''Một ngọn hải đăng đặt tại vị trí $A$ cách bờ biển một khoảng cách $AB = %s$ km. Trên bờ biển có một cái kho ở vị trí $C$ cách $B$ một khoảng là $%s$ km. Để nhận lương thực và các nhu yếu phẩm mỗi tháng, người canh hải đăng phải đi xuồng máy từ $A$ đến bến tàu $M$ trên bờ biển với vận tốc $%s$ km/h rồi đi xe gắn máy đến $C$ với vận tốc $%s$ km/h (xem hình vẽ).
            \\begin{center}
            \\begin{tikzpicture}[scale=0.3, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (B) at (0,0);
            \\coordinate (A) at (0,6);
            \\coordinate (C) at (15,0);
            \\coordinate (M) at (8,0);
            \\draw[thick] (A)--(B)--(C) (A)--(M);
            \\draw[dashed] (B)--(A) node[midway, left] {$%s$};
            \\draw (0,0.4)--(0.4,0.4)--(0.4,0);
            \\draw[<->] (0,-1.5)--(15,-1.5) node[midway, fill=white] {$%s$};
            \\draw (A) node[above] {$A$};
            \\draw (B) node[below left] {$B$};
            \\draw (M) node[below] {$M$};
            \\draw (C) node[below right] {$C$};
            \\end{tikzpicture}
            \\end{center}
            Tổng quãng đường người đó phải đi là bao nhiêu km? Biết rằng thời gian đi từ $A$ đến $C$ là %s.'''
                                 %(latex(ab), latex(bc), latex(v1), latex(v2), latex(ab), latex(bc), time_str))

                # Các đáp án trắc nghiệm
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

                # Lời giải chi tiết
                loigiai = ('''Ta có $%s = \\frac{%s}{%s}$ (h). Gọi $AM = x\\,\\text{(km)} (x > %s)$. \\\\
            Suy ra thời gian đi từ $A$ đến $M$ là $\\frac{x}{%s}$ (h). \\\\
            Khi đó $BM = \\sqrt{x^2 - %s^2} = \\sqrt{x^2 - %s}$ và $CM = %s - \\sqrt{x^2 - %s}$. \\\\
            Thời gian đi từ $M$ đến $C$ là $\\frac{%s - \\sqrt{x^2 - %s}}{%s}$. \\\\
            Theo giả thiết ta có phương trình: $\\frac{x}{%s} + \\frac{%s - \\sqrt{x^2 - %s}}{%s} = \\frac{%s}{%s}$. \\\\
            Giải phương trình ta được $x = %s\\,\\text{(km)}$. \\\\
            Do đó tổng quãng đường phải đi là $AM + MC = %s + \\left( %s - \\sqrt{%s^2 - %s} \\right) = %s\\,\\text{(km)}$.'''
                           %(time_str, latex(t_hour_frac.p), latex(t_hour_frac.q), latex(ab),
                             latex(v1), latex(ab), latex(ab**2), latex(bc), latex(ab**2),
                             latex(bc), latex(ab**2), latex(v2),
                             latex(v1), latex(bc), latex(ab**2), latex(v2), latex(t_hour_frac.p), latex(t_hour_frac.q),
                             latex(am_val), latex(am_val), latex(bc), latex(am_val), latex(ab**2), latex(s_val)
                            ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(s_val))
            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

