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


def bt_dang19_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # v(t) = v0 - a*t. Để kết quả đẹp, ta chọn t_dung (thời gian dừng) và gia tốc a trước.
                t_dung = random.randint(4, 8) # Thời gian từ lúc phanh đến khi dừng (giây)
                gia_toc_phanh = random.choice([Rational(5, 2), Rational(7, 2), 3, 4, 5]) 

                # Vận tốc ban đầu v0 = gia_toc_phanh * t_dung
                v0 = gia_toc_phanh * t_dung
                v0_float = float(v0)

                # Biểu thức v(t) = v0 - gia_toc_phanh * t
                # Viết dưới dạng phân số để giống mẫu trong ảnh
                v0_tex = latex(v0) if isinstance(v0, int) else latex(v0)
                a_tex = latex(gia_toc_phanh)

                # Bước 1 & 2: Tính toán quãng đường s(t_dung) = v0*t_dung - 0.5*a*t_dung^2
                t = symbols('t')
                v_func = v0 - gia_toc_phanh * t
                s_func = integrate(v_func, t) # Nguyên hàm (C=0 vì s(0)=0)

                dist_val = float(s_func.subs(t, t_dung))

                # Làm tròn đến hàng phần mười (0.1)
                kq_decimal = Decimal(str(dist_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % kq_str

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s_wrong = set()
                while len(s_wrong) < 3:
                    sai_offset = random.choice([-5.2, -3.5, 2.3, 4.7, 10.1, -10.5])
                    sai_val = float(kq_decimal) + sai_offset
                    sai_str = str(Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if sai_str != kq_str and float(sai_str.replace(',', '.')) > 0:
                        s_wrong.add('$%s$' % sai_str)

                list_wrong = list(s_wrong)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # Câu hỏi (Viết lại theo mẫu)
                noidungcauhoi = (r'''Một ô tô đang chạy với vận tốc $%s$ m/s thì người lái xe đạp phanh. Từ thời điểm đó ô tô chuyển động với vận tốc $v(t) = %s - %s t$ (m/s), trong đó $t$ (tính bằng giây) là thời gian kể từ lúc bắt đầu đạp phanh. Quãng đường ô tô di chuyển từ lúc đạp phanh đến khi dừng hẳn bằng bao nhiêu mét? (làm tròn kết quả đến hàng phần chục).'''
                                 % (str(v0_float).replace('.', ','), v0_tex, a_tex))

                # Nội dung lời giải (Bám sát hình ảnh Câu 13)
                loigiai = (r'''Ô tô dừng hẳn khi $v(t) = 0 \Leftrightarrow %s - %s t = 0 \Leftrightarrow t = %s$ (giây). \\
                             Quãng đường ô tô di chuyển từ lúc đạp phanh là \\
                             $s(t) = \int v(t) \text{d}t = \int \left( %s - %s t \right) \text{d} t = %s t - \frac{%s}{2} t^2 + C$. \\
                             Ta có $s(0) = 0$, suy ra $C = 0$, do đó $s(t) = %s t - %s t^2$. \\
                             Do đó $s(%s) = %s \cdot %s - %s \cdot %s^2 \approx %s$ (m).'''
                           % (v0_tex, a_tex, t_dung,
                              v0_tex, a_tex, v0_tex, a_tex,
                              v0_tex, latex(gia_toc_phanh/2),
                              t_dung, v0_tex, t_dung, latex(gia_toc_phanh/2), t_dung, kq_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

