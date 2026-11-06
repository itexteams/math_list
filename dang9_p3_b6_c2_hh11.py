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


def bt_dang9_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random số a là một số cụ thể
                a_val = random.choice([2, 4, 6, 8])

                # Bước 2: Xác định hệ số k
                k_val = random.choice([1, 2, 3, 4, 5])

                # Tính thể tích V (số hữu tỷ)
                v_val = Rational(k_val * a_val**2, 4)
                v_tex = latex(v_val)

                # Tính SA = k * sqrt(3) và làm tròn đến hàng phần chục
                # Sử dụng math.sqrt hoặc lũy thừa 0.5 để tính toán số thực
                sa_real_val = float(k_val * 3**0.5)
                da_dung_val = round(sa_real_val, 1)
                da_dung = "$%s$" % da_dung_val

                # Tạo các đáp án sai (nhiễu) cũng làm tròn đến hàng phần chục
                s = []
                while len(s) < 3:
                    k_fake = random.randint(1, 10)
                    if k_fake != k_val:
                        fake_val = round(float(k_fake * 3**0.5), 1)
                        option = "$%s$" % fake_val
                        if option not in s and fake_val != da_dung_val:
                            s.append(option)

                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                # Câu hỏi: Thay a bằng số cụ thể
                noidungcauhoi = ("Cho hình chóp $S.ABC$ có đáy là tam giác đều cạnh bằng $%s$, cạnh bên $SA$ vuông góc với đáy và thể tích của khối chóp đó bằng $%s$. Cạnh bên $SA$ bằng bao nhiêu? (làm tròn đến hàng phần chục)." 
                                 % (a_val, v_tex))

                # TikZ code cho hình vẽ
                tikz_code = ("""\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, line width=1pt]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.2,-1.2);
                \\coordinate (C) at (3.5,0);
                \\coordinate (S) at (0,3);
                \\draw [dashed] (A)--(C);
                \\draw (S)--(A)--(B)--(C)--(S)--(B);
                \\draw (0,0) node[left] {$A$} (1.2,-1.2) node[below] {$B$} (3.5,0) node[right] {$C$} (0,3) node[above] {$S$};
            \\end{tikzpicture}
            \\end{center}""")

                # Nội dung lời giải chi tiết
                s_day_val = Rational(a_val**2, 4)
                s_day_tex = "%s\\sqrt{3}" % s_day_val if s_day_val != 1 else "\\sqrt{3}"

                loigiai = (tikz_code + 
                           "Diện tích đáy là tam giác đều cạnh $%s$ là $S_{\\triangle ABC} = \\frac{%s^2\\sqrt{3}}{4} = %s$.\\\\ " 
                           % (a_val, a_val, s_day_tex) +
                           "Ta có thể tích khối chóp $V_{S.ABC} = \\frac{1}{3} \\cdot S_{\\triangle ABC} \\cdot SA$.\\\\ " +
                           "Suy ra $SA = \\frac{3V_{S.ABC}}{S_{\\triangle ABC}} = \\frac{3 \\cdot %s}{%s} = %s \\approx %s$." 
                           % (v_tex, s_day_tex, latex(k_val * sqrt(3)), da_dung_val))

                # Sửa lỗi kqz bằng cách dùng da_dung_val
                dapan='\\shortans[0]{$%s$}\n'%(str(da_dung_val).replace('.', ','))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = ["\\True " + da_dung, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

