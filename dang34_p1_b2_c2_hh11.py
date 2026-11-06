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


def bt_dang34_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Danh sách các bộ đỉnh có thể dùng để thay đổi
            danh_sach_dinh = [
                ('A', 'B', 'C', 'D', 'M', 'N'),
            ]

            # Chọn ngẫu nhiên một bộ tên gọi
            v1, v2, v3, v4, m1, n1 = random.choice(danh_sach_dinh)

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho tứ diện đều $%s%s%s%s$ có $%s, %s$ lần lượt là trung điểm của các cạnh $%s%s$ và $%s%s$. Mệnh đề nào sau đây \\textbf{sai}?'
                % (v1, v2, v3, v4, m1, n1, v1, v2, v3, v4)
            )

            # Các mệnh đề
            da_dung = '$%s%s \\perp %s%s$' % (m1, n1, v2, v4) # Mệnh đề SAI (Đáp án cần chọn)
            s1 = '$%s%s \\perp %s%s$' % (m1, n1, v1, v2)      # Mệnh đề đúng
            s2 = '$%s%s \\perp %s%s$' % (m1, n1, v3, v4)      # Mệnh đề đúng
            s3 = '$%s%s \\perp %s%s$' % (v1, v2, v3, v4)      # Mệnh đề đúng

            # Bước 4: Điều chỉnh các phương án và trộn ngẫu nhiên
            da_d = '\\True ' + da_dung
            list_ans = [da_d, s1, s2, s3]
            random.shuffle(list_ans)

            # Vẽ hình bằng TikZ (độ dày 1pt)
            ve_hinh = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, line width=1pt]\n'
                '  \\coordinate (A) at (1.5,4);\n'
                '  \\coordinate (B) at (0,0);\n'
                '  \\coordinate (C) at (4,1);\n'
                '  \\coordinate (D) at (2,-1);\n'
                '  \\coordinate (M) at ($(A)!0.5!(B)$);\n'
                '  \\coordinate (N) at ($(C)!0.5!(D)$);\n'
                '  \\draw [line width=1pt] (A)--(B)--(D)--(A);\n'
                '  \\draw [line width=1pt] (A)--(C)--(D);\n'
                '  \\draw [dashed, line width=1pt] (B)--(C);\n'
                '  \\draw [dashed, line width=1pt] (M)--(N);\n'
                '  \\draw [dashed, line width=1pt] (A)--(N);\n'
                '  \\draw [dashed, line width=1pt] (B)--(N);\n'
                '  \\draw [line width=1pt] (M)--(C);\n'
                '  \\draw [line width=1pt] (M)--(D);\n'
                '  \\draw (A) node[above] {$%s$};\n'
                '  \\draw (B) node[left] {$%s$};\n'
                '  \\draw (C) node[right] {$%s$};\n'
                '  \\draw (D) node[below] {$%s$};\n'
                '  \\draw (M) node[left] {$%s$};\n'
                '  \\draw (N) node[right] {$%s$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}' % (v1, v2, v3, v4, m1, n1)
            )

            # Lời giải chi tiết
            loigiai = (
                '\\begin{itemize}\n'
                '    \\item $\\triangle %s%s%s$ cân tại $%s$ (do $%s%s = %s%s$ là hai đường cao của các tam giác đều bằng nhau) nên $%s%s \\perp %s%s$.\n'
                '    \\item $\\triangle %s%s%s$ cân tại $%s$ (do $%s%s = %s%s$) nên $%s%s \\perp %s%s$.\n'
                '    \\item Ta có $%s%s \\perp %s%s$ và $%s%s \\perp %s%s$ nên $%s%s \\perp \\left(%s%s%s\\right) \\Rightarrow %s%s \\perp %s%s$.\n'
                '    \\item Giả sử $%s%s \\perp %s%s$. Mà $%s%s \\perp %s%s$, suy ra $%s%s \\perp \\left(%s%s%s\\right)$. Điều này là vô lý vì $%s%s%s%s$ là tứ diện đều.\n'
                '\\end{itemize}\n'
                'Vậy phương án $%s%s \\perp %s%s$ là mệnh đề sai.'
                % (n1, v1, v2, n1, n1, v1, n1, v2, m1, n1, v1, v2,
                   m1, v3, v4, m1, m1, v3, m1, v4, m1, n1, v3, v4,
                   v3, v4, n1, v1, v3, v4, n1, v2, v3, v4, v1, v2, n1, v3, v4, v1, v2,
                   m1, n1, v2, v4, m1, n1, v1, v2, m1, n1, v1, v2, v4, v1, v2, v3, v4,
                   m1, n1, v2, v4)
            )

            # Xuất câu trắc nghiệm (Không dùng raw string r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + ve_hinh + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

