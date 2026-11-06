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


def bt_dang21_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3 - Random bài toán
                # Ta giữ nguyên hình dáng của hàm số bậc 3 như đồ thị (đạt cực đại tại x = 1, cực tiểu tại x = -1).
                # Phương trình hàm số có dạng tổng quát: y = -k*x^3/2 + 3*k*x/2 + ymid
                # Trong đó m là giá trị nhỏ nhất, M là giá trị lớn nhất trên [-2; 2].

                m = random.randint(-2, 1)      # Giá trị cực tiểu
                k = random.randint(1, 3)       # Hệ số co giãn
                M = m + 2 * k                  # Giá trị cực đại
                ymid = m + k                   # Giá trị tại x = 0 (Giao điểm với trục tung)

                # Tính giới hạn trục tọa độ để vẽ hình cho đẹp
                ymin_ax = min(-1, m - 1)
                ymax_ax = max(1, M + 1)

                # B4 - Điều chỉnh các nét đứt và nhãn dán trên đồ thị tương ứng với các số random
                dash_M = "\\draw[dashed] (-2,0) -- (-2,%s) -- (1,%s) -- (1,0);" % (M, M)
                dash_m = ""
                if m != 0:
                    dash_m = "\\draw[dashed] (-1,0) -- (-1,%s) -- (2,%s) -- (2,0);" % (m, m)

                y_labels = ""
                if M != 0: 
                    y_labels += "\\draw (0.1,%s) -- (-0.1,%s) node[left] {$%s$};" % (M, M, M)
                if m != 0: 
                    y_labels += "\\draw (0.1,%s) -- (-0.1,%s) node[left] {$%s$};" % (m, m, m)
                if ymid != 0 and ymid != M and ymid != m: 
                    y_labels += "\\draw (0.1,%s) -- (-0.1,%s) node[left] {$%s$};" % (ymid, ymid, ymid)

                # Đoạn code TikZ vẽ đồ thị 
                tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, x=1cm, y=1cm]
            \\draw[->] (-3,0) -- (3,0) node[below] {$x$};
            \\draw[->] (0,%s) -- (0,%s) node[right] {$y$};
            \\node[below right] at (0,0) {$O$};
            \\foreach \\x in {-2, -1, 1, 2} {
                \\draw (\\x,0.1) -- (\\x,-0.1) node[below] {$\\x$};
            }
            %s
            %s
            %s
            \\draw[line width=1pt, domain=-2.2:2.2, smooth, samples=100] plot (\\x, {-(%s)*\\x*\\x*\\x/2 + 3*(%s)*\\x/2 + %s});
            \\fill (-2,%s) circle (1.5pt);
            \\fill (-1,%s) circle (1.5pt);
            \\fill (0,%s) circle (1.5pt);
            \\fill (1,%s) circle (1.5pt);
            \\draw[fill=white] (2,%s) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}''' % (ymin_ax, ymax_ax, dash_M, dash_m, y_labels, k, k, ymid, M, m, ymid, M, m))

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = f(x)$ liên tục trên đoạn $[-2; 2]$ và có đồ thị như hình vẽ bên.
            %s
            Gọi $M, m$ lần lượt là giá trị lớn nhất và nhỏ nhất của hàm số đã cho trên đoạn $[-2; 2]$. Giá trị $M + m$ là''' % tikz_code)

                # Tính toán đáp án
                ans = M + m
                da = str(ans)

                # Tạo các phương án nhiễu sai khác đáp án đúng
                choices = [ans + 1, ans - 1, ans + 2, ans - 2, M, m, M - m]
                choices = list(set(choices) - {ans})
                das = random.sample(choices, 3)

                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das[0])
                da_s2 = ('$%s$' % das[1])
                da_s3 = ('$%s$' % das[2])

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                m_str = '(%s)' % m if m < 0 else str(m)
                loigiai = ('''Quan sát đồ thị hàm số trên đoạn $[-2; 2]$, ta thấy: \\\\
            + Điểm cao nhất của đồ thị có tung độ bằng $%s$, đạt được tại $x = -2$ và $x = 1$. Suy ra giá trị lớn nhất của hàm số là $M = %s$. \\\\
            + Điểm thấp nhất của đồ thị có tung độ bằng $%s$, đạt được tại $x = -1$. Suy ra giá trị nhỏ nhất của hàm số là $m = %s$. \\\\
            Vậy $M + m = %s + %s = %s$.''' % (M, M, m, m, M, m_str, ans))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

