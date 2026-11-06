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


def bt_dang11_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các thiết lập ban đầu
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thông thường bài toán này kết quả luôn là 90 độ do tính chất hình vuông
                # Để "random" ta có thể thay đổi tên các đỉnh, nhưng ở đây giữ nguyên theo hình ảnh mẫu

                # Đáp án đúng
                kq = 90
                du = ['$%s^\\circ$' % (latex(kq))]
                da = random.choice(du)

                # Các phương án nhiễu
                s = ['$30^\\circ$', '$45^\\circ$', '$60^\\circ$', '$120^\\circ$']

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Hình vẽ TikZ cho hình hộp chữ nhật có đáy là hình vuông
                tikz = r'''\begin{tikzpicture}[line cap=round,line join=round,scale=0.7]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.2,1.2);
                \coordinate (D) at (4,0);
                \coordinate (C) at (5.2,1.2);
                \coordinate (A1) at (0,4);
                \coordinate (B1) at (1.2,5.2);
                \coordinate (D1) at (4,4);
                \coordinate (C1) at (5.2,5.2);
                \draw [dashed] (A)--(B)--(C) (B)--(B1);
                \draw (A)--(D)--(C)--(C1)--(B1)--(A1)--cycle;
                \draw (A1)--(D1)--(C1) (D)--(D1);
                \draw [dashed, blue, thick] (A1)--(C);
                \draw [dashed, blue, thick] (B)--(D);
                \draw[fill=black] (A) node[left]{$A$};
                \draw[fill=black] (B) node[below right]{$B$};
                \draw[fill=black] (C) node[right]{$C$};
                \draw[fill=black] (D) node[right]{$D$};
                \draw[fill=black] (A1) node[left]{$A'$};
                \draw[fill=black] (B1) node[above]{$B'$};
                \draw[fill=black] (C1) node[right]{$C'$};
                \draw[fill=black] (D1) node[above]{$D'$};
                \end{tikzpicture}'''

                # Câu hỏi
                noidungcauhoi = ('''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$, biết đáy $ABCD$ là hình vuông. Tính góc giữa $A'C$ và $BD$.
                \\begin{center}
                %s
                \\end{center}''' % (tikz))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo đúng hình ảnh
                loigiai = ('''Đặt $\\overrightarrow{A'B'} = \\vec{a}$, $\\overrightarrow{A'D'} = \\vec{b}$, $\\overrightarrow{A'A} = \\vec{c}$, $AB = x$. \\\\
                             Ta có $\\overrightarrow{A'C} = \\overrightarrow{A'B'} + \\overrightarrow{A'D'} + \\overrightarrow{A'A} = \\vec{a} + \\vec{b} + \\vec{c}$. \\\\
                             Lại có $\\overrightarrow{BD} = \\overrightarrow{AD} - \\overrightarrow{AB} = \\vec{b} - \\vec{a}$. \\\\
                             Xét tích vô hướng: \\\\
                             $\\overrightarrow{A'C} \\cdot \\overrightarrow{BD} = (\\vec{a} + \\vec{b} + \\vec{c}) \\cdot (\\vec{b} - \\vec{a})$ \\\\
                             $= \\vec{a} \\cdot \\vec{b} - (\\vec{a})^2 + (\\vec{b})^2 - \\vec{b} \\cdot \\vec{a} + \\vec{c} \\cdot \\vec{b} - \\vec{c} \\cdot \\vec{a}$. \\\\
                             Vì $ABCD.A'B'C'D'$ là hình hộp chữ nhật nên các cặp vectơ $(\\vec{a}, \\vec{b})$, $(\\vec{b}, \\vec{c})$, $(\\vec{c}, \\vec{a})$ đôi một vuông góc, do đó tích vô hướng của chúng bằng $0$. \\\\
                             Mặt khác, vì $ABCD$ là hình vuông nên $|\\vec{a}| = |\\vec{b}| = x$. \\\\
                             Suy ra: $\\overrightarrow{A'C} \\cdot \\overrightarrow{BD} = 0 - x^2 + x^2 - 0 + 0 - 0 = 0$. \\\\
                             Vậy $\\overrightarrow{A'C} \\perp \\overrightarrow{BD}$ hay góc giữa $A'C$ và $BD$ bằng $90^\\circ$.''')

            # Xuất câu trắc nghiệm
            # Không dùng tiền tố r (raw string) trong phần content theo yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +  
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

