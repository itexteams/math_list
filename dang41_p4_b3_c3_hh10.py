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


def bt_dang41_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM DỮ LIỆU ĐỂ ĐẢM BẢO NGHIỆM ĐẸP (t=0) ---
                # Trong bài mẫu: d: x-y-1=0, C1: (x-3)^2+(y+4)^2=8, C2: (x+5)^2+(y-4)^2=32
                # Tôi sẽ giữ cấu trúc nhưng có thể thay đổi các hằng số m, x1, y1...

                m = random.choice([-1, 1, 2]) # Hệ số tự do của d: x - y + m = 0
                t_fixed = 0 # Giả định giải ra t = 0 cho đẹp

                # Tâm I_1(x1, y1), I_2(x2, y2). Để t=0 là nghiệm, ta thiết lập khoảng cách phù hợp.
                # Ở đây tôi chọn bộ số tương tự mẫu để bảo đảm tính logic hình học
                x1, y1 = 3, -4
                x2, y2 = -5, 4
                R1_sq = 8   # R1 = 2*sqrt(2)
                R2_sq = 32  # R2 = 4*sqrt(2)

                R1 = sqrt(R1_sq)
                R2 = sqrt(R2_sq)

                # Phương trình đường thẳng d: x - y + m = 0 (m=-1 trong ảnh)
                # I thuộc d => I(t, t+m)

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $d: x - y %s = 0$ và hai đường tròn $(C_1): (x-%s)^2 + (y-%s)^2 = %s$; $(C_2): (x-%s)^2 + (y-%s)^2 = %s$. Lập phương trình đường tròn $(C)$ có tâm $I$ thuộc $d$ và tiếp xúc ngoài với hai đường tròn trên.'''
                                % (('+' + str(m) if m > 0 else str(m)), x1, y1, R1_sq, x2, y2, R2_sq))

                # --- BƯỚC 2: GIẢI CHI TIẾT ---
                # I(t; t+m) -> I(0; -1) nếu m=-1
                # II1 = sqrt((t-x1)^2 + (t+m-y1)^2)
                # II2 = sqrt((t-x2)^2 + (t+m-y2)^2)

                y_I_expr = "t" + (f"+{m}" if m > 0 else f"{m}")

                # Biểu thức trong căn của II1 và II2 (sau khi thay y = t+m)
                expr1 = simplify((t_fixed - x1)**2 + (t_fixed + m - y1)**2) # Tại t=0
                expr2 = simplify((t_fixed - x2)**2 + (t_fixed + m - y2)**2) # Tại t=0

                dist1 = sqrt(expr1)
                dist2 = sqrt(expr2)
                R_val = dist1 - R1

                # Phương trình cuối cùng
                kq_chuan = r"x^2 + (y%s)^2 = %s" % (("-" + str(t_fixed + m) if (t_fixed + m) > 0 else "+" + str(-(t_fixed + m))), latex(R_val**2))

                # --- BƯỚC 3: TẠO ĐÁP ÁN ---
                da_d = '\\True $' + kq_chuan + '$'

                s = [
                    '$x^2 + (y-2)^2 = 4$',
                    '$x^2 + (y+1)^2 = 4$',
                    '$(x-1)^2 + y^2 = 2$',
                    '$(x+2)^2 + (y-1)^2 = 8$',
                    '$x^2 + (y-1)^2 = 2$'
                ]
                random.shuffle(s)
                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- LỜI GIẢI ---
                loigiai = (r'''Gọi $I, I_1, I_2, R, R_1, R_2$ lần lượt là tâm và bán kính của 3 đường tròn $(C), (C_1)$ và $(C_2)$. \\
            Giả sử $I(t; %s) \in d$. Theo giả thiết bài toán: $(C)$ tiếp xúc ngoài $(C_1)$ và $(C_2)$ nên: \\
            $\begin{cases} II_1 = R + R_1 \\ II_2 = R + R_2 \end{cases}$ \\
            Suy ra $II_1 - R_1 = II_2 - R_2$ \\
            $\Leftrightarrow \sqrt{(t-%s)^2 + (t%s)^2} - %s = \sqrt{(t-%s)^2 + (t%s)^2} - %s$ \\
            $\Leftrightarrow t = 0$ \\
            Với $t=0$ suy ra $I(0; %s)$ và $R = %s$. \\
            Phương trình đường tròn $(C): %s$.''' 
                % (y_I_expr, x1, ("+" + str(m-y1) if m-y1 > 0 else str(m-y1)), latex(R1), 
                   x2, ("+" + str(m-y2) if m-y2 > 0 else str(m-y2)), latex(R2), 
                   m, latex(R_val), kq_chuan))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+')
            return content

