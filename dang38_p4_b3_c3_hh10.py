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


def bt_dang38_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # --- BƯỚC 3: TƯ DUY RANDOM BÀI TOÁN ---
            x1, y1 = random.randint(-3, 3), random.randint(-3, 3)
            x2, y2 = random.randint(-3, 3), random.randint(-3, 3)

            while (x1, y1) == (x2, y2):
                x2, y2 = random.randint(-3, 3), random.randint(-3, 3)

            d2 = (x2 - x1)**2 + (y2 - y1)**2
            d_val = simplify(f"sqrt({d2})")

            r1_sq = d2
            r2_sq = 4 * d2 

            # --- BƯỚC 1 & 2: GIẢI CHI TIẾT ---
            c1_expr = (x - x1)**2 + (y - y1)**2
            c2_expr = (x - x2)**2 + (y - y2)**2

            # Tọa độ tiếp điểm M
            line_eq = simplify(c1_expr - r1_sq - (c2_expr - r2_sq))
            sol = solve([line_eq, c1_expr - r1_sq], [x, y])
            xm, ym = sol[0]

            # Vectơ pháp tuyến
            a_tp = x2 - x1
            b_tp = y2 - y1

            # SỬA LỖI TẠI ĐÂY: Sử dụng expand trực tiếp sau khi đã import
            tt_expr = expand(a_tp*(x - xm) + b_tp*(y - ym))

            if a_tp < 0 or (a_tp == 0 and b_tp < 0):
                tt_expr = tt_expr * -1

            # Nội dung câu hỏi
            noidungcauhoi = (r"Trong mặt phẳng tọa độ $Oxy$, cho hai đường tròn $(C_1): %s = %s$ và $(C_2): %s = %s$. Lập phương trình tiếp tuyến chung của hai đường tròn." 
                             % (latex(c1_expr), latex(r1_sq), latex(c2_expr), latex(r2_sq)))

            # Đáp án
            da_dung = "$%s = 0$" % latex(tt_expr)
            da_s1 = "$%s = 0$" % latex(tt_expr + random.randint(1, 5))
            da_s2 = "$%s = 0$" % latex(tt_expr - random.randint(1, 5))
            da_s3 = "$%s = 0$" % latex(expand(b_tp*x - a_tp*y + random.randint(-5, 5)))

            list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải
            loigiai = (r"$(C_1)$ có tâm $I_1(%s; %s)$ và bán kính $R_1 = %s$. \\ "
                       r"$(C_2)$ có tâm $I_2(%s; %s)$ và bán kính $R_2 = %s$. \\ "
                       r"Ta có $I_1I_2 = %s = |R_2 - R_1|$, do đó hai đường tròn tiếp xúc trong. Như vậy có 1 tiếp tuyến chung. \\ "
                       r"Tọa độ tiếp điểm $M$ là nghiệm của hệ: \\ "
                       r"$\begin{cases} %s = %s \\ %s = %s \end{cases} \Rightarrow M(%s; %s)$. \\ "
                       r"Tiếp tuyến chung $\Delta$ qua $M(%s; %s)$ và nhận $\overrightarrow{I_1I_2} = (%s; %s)$ làm VTPT: $\Delta: %s = 0$."
                       % (x1, y1, latex(simplify(f"sqrt({r1_sq})")), 
                          x2, y2, latex(simplify(f"sqrt({r2_sq})")), 
                          latex(d_val),
                          latex(c1_expr), r1_sq, latex(c2_expr), r2_sq, xm, ym,
                          xm, ym, a_tp, b_tp, latex(tt_expr)))

            loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

