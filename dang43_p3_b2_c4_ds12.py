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


def bt_dang43_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số đầu bài
                # p_thethao: % tổng số học sinh tham gia thể thao
                p_thethao = random.choice([50, 55, 60, 65])
                p_vannghe = 100 - p_thethao

                # p_nam_thethao: % số bạn nam tham gia thể thao (phải lớn hơn p_thethao để x > 0)
                p_nam_thethao = random.choice([70, 75, 80, 85, 90])
                while p_nam_thethao <= p_thethao:
                    p_nam_thethao = random.choice([70, 75, 80, 85, 90])

                p_nam_vannghe = 100 - p_nam_thethao

                # Chuyển sang số thập phân để tính toán
                pB = Rational(p_thethao, 100)        # P(B) - tham gia thể thao
                pB_not = Rational(p_vannghe, 100)    # P(B gạch đầu) - tham gia văn nghệ
                pB_cond_A_not = Rational(p_nam_thethao, 100) # P(B|A gạch đầu) - Nam tham gia thể thao

                # Giải phương trình P(B) = P(A).P(B|A) + P(not A).P(B|not A)
                # 0.6 = x*0 + (1-x)*0.8 => x = 0.25
                x_val = symbols('x')
                eq = Eq(pB, x_val * 0 + (1 - x_val) * pB_cond_A_not)
                sol_x = solve(eq, x_val)[0] # Xác suất học sinh là nữ P(A)

                # Tính xác suất hậu nghiệm P(A|B_not) = [P(A)*P(B_not|A)] / P(B_not)
                # Vì nữ đều tham gia văn nghệ nên P(B_not|A) = 1
                tu_so = sol_x * 1
                mau_so = pB_not
                kq_fraction = tu_so / mau_so

                # Làm tròn đến hàng phần trăm theo yêu cầu (0,63)
                kq_float = float(kq_fraction)
                kq_rounded = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Định dạng hiển thị dấu phẩy cho số thập phân
                da_dung = str(kq_rounded).replace('.', ',')

                # Tạo các phương án sai
                s = []
                offsets = [-0.12, 0.15, -0.08, 0.22, -0.18, 0.07]
                for offset in offsets:
                    val = float(kq_rounded) + offset
                    if 0 < val < 1:
                        s.append(str(Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Nhân dịp kỷ niệm 10 năm thành lập trường, các học sinh lựa chọn tham gia thi đấu thể thao hoặc biểu diễn văn nghệ. Lớp 12A1 có $%s\\%%$ số học sinh tham gia thi đấu thể thao và còn lại $%s\\%%$ tham gia biểu diễn văn nghệ. Biết rằng các bạn nữ đều tham gia biểu diễn văn nghệ. Trong số các bạn nam có $%s\\%%$ tham gia văn nghệ và $%s\\%%$ tham gia thi đấu thể thao. Chọn ngẫu nhiên một học sinh trong lớp 12A1. Biết rằng học sinh này tham gia biểu diễn văn nghệ, xác suất để học sinh này là nữ là bao nhiêu? (Nếu kết quả là số thập phân thì làm tròn đến hàng phần trăm).'
                                 % (latex(p_thethao), latex(p_vannghe), latex(p_nam_vannghe), latex(p_nam_thethao)))

                # Các đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('Gọi $A$: "Học sinh nữ" \\\\ '
                           '$\\overline{A}$: "Học sinh nam" \\\\ '
                           '$B$: "Học sinh tham gia thi đấu thể thao" \\\\ '
                           '$\\overline{B}$: "Học sinh tham gia biểu diễn văn nghệ" \\\\ '
                           'Giả sử $P(A) = x, 0 \\le x \\le 1$. \\\\ '
                           'Ta có $P(B) = P(A) \\cdot P(B|A) + P(\\overline{A}) \\cdot P(B|\\overline{A})$ \\\\ '
                           '$\\Rightarrow 0 \\cdot x + %s \\cdot (1-x) = %s \\Rightarrow x = %s$. \\\\ '
                           'Vậy xác suất để học sinh được chọn là nữ, biết học sinh này tham gia biểu diễn văn nghệ là \\\\ '
                           '$P(A|\\overline{B}) = \\frac{P(A) \\cdot P(\\overline{B}|A)}{P(\\overline{B})} = \\frac{%s \\cdot 1}{%s} = %s \\approx %s$.'
                           % (str(float(pB_cond_A_not)).replace('.', ','), 
                              str(float(pB)).replace('.', ','), 
                              str(float(sol_x)).replace('.', ','),
                              str(float(sol_x)).replace('.', ','),
                              str(float(pB_not)).replace('.', ','),
                              latex(kq_fraction),
                              da_dung))
                dapan=' \\shortans[0]{$%s$} '%(da_dung)
            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

