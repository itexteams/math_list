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


def bt_dang12_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các bộ số (b, d) sao cho d^2 + b^2 là số chính phương để m đẹp
                # Công thức: Delta = b^2 - 4m(m + d) = -4m^2 - 4dm + b^2
                # Nghiệm của -4m^2 - 4dm + b^2 = 0 là m = (-d \pm sqrt(d^2 + b^2)) / 2
                triples = [(4, 3), (8, 6), (12, 5), (12, 9), (15, 8)]
                b_val, d_val = random.choice(triples)

                # Random dấu cho b
                b_val = b_val * random.choice([1, -1])

                # Tính toán k = sqrt(d^2 + b^2)
                k = int((d_val**2 + b_val**2)**0.5)

                # Tính 2 nghiệm m1, m2 (m1 < m2)
                m1 = Rational(-d_val - k, 2)
                m2 = Rational(-d_val + k, 2)

                base = random.choice([2, 3, 5]) # Cơ số logarit

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (r'Tìm giá trị của tham số $m$ để hàm số $y = \frac{1}{m\log_{%s}^2 x %s \log_{%s} x + m + %s}$ xác định trên khoảng $(0;+\infty)$.'
                                 % (latex(base), 
                                    '+ ' + str(b_val) if b_val > 0 else str(b_val), 
                                    latex(base), 
                                    latex(d_val)))

                # --- Đáp án đúng ---
                da_dung = r'm \in (-\infty; %s) \cup (%s; +\infty)' % (latex(m1), latex(m2))
                da_d = r'\True $%s$' % da_dung

                # --- Các đáp án sai (Điều chỉnh để không trùng đáp án đúng) ---
                s = [
                    r'm \in (%s; %s)' % (latex(m1), latex(m2)), # Khoảng giữa
                    r'm \in (-\infty; %s] \cup [%s; +\infty)' % (latex(m1), latex(m2)), # Ngoặc vuông
                    r'm \in (-\infty; %s) \cup (%s; +\infty)' % (latex(m1-1), latex(m2+1)), # Lệch giá trị
                    r'm \in (%s; +\infty)' % (latex(m2)), # Thiếu một vế
                    r'm \in \mathbb{R}',
                    r'm \in \varnothing'
                ]

                random.shuffle(s)
                da_s1 = '$%s$' % s[0]
                da_s2 = '$%s$' % s[1]
                da_s3 = '$%s$' % s[2]

                # Trộn các đáp án
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # --- Nội dung lời giải ---
                loigiai = (r'''Để hàm số xác định trên khoảng $(0;+\infty)$ thì phương trình $m\log_{%s}^2 x %s \log_{%s} x + m + %s = 0$ vô nghiệm với mọi $x > 0$. \\
                            Đặt $t = \log_{%s} x$. Khi $x \in (0;+\infty)$ thì $t \in \mathbb{R}$. \\
                            Phương trình trở thành: $mt^2 %s t + m + %s = 0$ (*) vô nghiệm trên $\mathbb{R}$. \\
                            \textbf{TH1:} $m = 0$. Phương trình (*) trở thành: $%s t + %s = 0 \Leftrightarrow t = %s$. \\
                            Vậy $m = 0$ không thỏa mãn. \\
                            \textbf{TH2:} $m \neq 0$. Phương trình (*) vô nghiệm khi: \\
                            $\Delta = (%s)^2 - 4m(m + %s) < 0$ \\
                            $\Leftrightarrow -4m^2 - %sm + %s < 0$ \\
                            $\Leftrightarrow m < %s$ hoặc $m > %s$. \\
                            Vậy $m \in (-\infty; %s) \cup (%s; +\infty)$.''' 
                            % (latex(base), '+ ' + str(b_val) if b_val > 0 else str(b_val), latex(base), latex(d_val),
                               latex(base),
                               '+ ' + str(b_val) if b_val > 0 else str(b_val), latex(d_val),
                               str(b_val), latex(d_val), latex(Rational(-d_val, b_val)),
                               str(b_val), latex(d_val),
                               latex(4*d_val), latex(b_val**2),
                               latex(m1), latex(m2),
                               latex(m1), latex(m2)
                            ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

