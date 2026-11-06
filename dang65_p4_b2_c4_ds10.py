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


def bt_dang65_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn a sao cho h(0.5) đẹp (a chia hết cho 4)
                a = random.choice([-16, -12, -8, -4]) 
                b = random.randint(40, 80) 
                c = 0

                def h(t_val):
                    return a * (t_val**2) + b * t_val + c

                # Các giá trị tính toán
                h_0 = h(0)
                h_05 = h(0.5)
                h_1 = h(1)
                h_2 = h(2)
                kq_val = h(3)

                # Hàm hỗ trợ format số: chuyển float sang chuỗi và thay . thành ,
                def fmt(val):
                    # Nếu là số nguyên thì latex bình thường, nếu số thực thì thay dấu
                    return latex(val).replace('.', ',')

                # Đáp án đúng
                kq = '$%s$' % fmt(kq_val)

                # Tạo các đáp án nhiễu
                s = set()
                while len(s) < 3:
                    sai = kq_val + random.choice([-20, -10, 10, 15, 20, -15, 5])
                    if sai != kq_val and sai > 0:
                        s.add('$%s$' % fmt(sai))

                list_sai = list(s)
                da_d = '\\True ' + kq
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi (đã sửa 0.5 thành 0,5 và dùng hàm fmt)
                noidungcauhoi = (r'''Độ cao của quả bóng golf tính theo thời gian có thể được xác định bằng một hàm bậc hai. Với các thông số cho trong bảng sau:
            \begin{center}
            \begin{tabular}{|c|c|c|c|c|}
            \hline
            Thời gian (giây) & $0$ & $0,5$ & $1$ & $2$ \\ \hline
            Độ cao (mét) & $%s$ & $%s$ & $%s$ & $%s$ \\ \hline
            \end{tabular}
            \end{center}
            Tính độ cao quả bóng đạt được tại thời điểm $3$ giây.''' 
                                 % (fmt(h_0), fmt(h_05), fmt(h_1), fmt(h_2)))

                # Nội dung lời giải chi tiết (Dùng fmt cho tất cả các giá trị số)
                loigiai = (r'''Độ cao của quả bóng tính theo thời gian được xác định bởi hàm số $h(t) = at^2 + bt + c$ (tính bằng mét), $t$: giây, $t \ge 0$. \\
            Với các thông số cho bởi bảng trên ta có hệ phương trình:
            $\begin{cases} c = %s \\ \frac{1}{4}a + \frac{1}{2}b + c = %s \\ a + b + c = %s \\ 4a + 2b + c = %s \end{cases} \Leftrightarrow \begin{cases} a = %s \\ b = %s \\ c = %s \end{cases}$ \\
            $\Rightarrow h(t) = %st^2 + %st \Rightarrow h(3) = %s$. \\
            Vậy độ cao quả bóng đạt được tại thời điểm $3$ giây là $%s$ m.''' 
                           % (fmt(c), fmt(h_05), fmt(h_1), fmt(h_2), 
                              fmt(a), fmt(b), fmt(c), 
                              fmt(a), fmt(b), fmt(kq_val), fmt(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

