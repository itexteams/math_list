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


def bt_dang61_p1_b3_c3_ds12(self):
            # Khai báo biến
            # x2: cận trên
            base = random.choice([2, 3])
            x1 = random.randint(1, 2)
            delta = random.randint(1, 2)
            x2 = x1 + delta
            k = base ** x1 # Giá trị của hàm số tại x1
            k_val = base ** x2 # Giá trị của hàm số tại x2

            # Tạo hình vẽ TikZ
            tikz_code = (r'''\begin{center} \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (304.9,64.4) .. controls (304.9,102.4) and (305.9,173.4) .. (305.4,205.4) .. controls (284.9,205.9) and (284.4,205.4) .. (255.9,206.4) .. controls (279.4,173.9) and (294.9,120.9) .. (304.9,64.4) -- cycle ;
            	\draw [line width=1]    (146.4,252.4) -- (393.4,252.89) ;
            	\draw [shift={(397.4,252.9)}, rotate = 180.11] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw [line width=1]    (230.9,281.4) -- (230.9,35.9) ;
            	\draw [shift={(230.9,31.9)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (255.9,206.4) -- (231.4,204.9) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (256.4,252.4) -- (255.9,206.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (305.9,251.4) -- (305.4,205.4) ;
            	\draw [line width=1]    (255.9,206.4) -- (305.4,205.4) ;
            	\draw [line width=1]    (305.4,205.4) -- (304.9,64.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (304.9,64.4) -- (230.4,64.4) ;
            	\draw [line width=1]    (148.5,249.5) .. controls (258.9,251.9) and (287.4,169.9) .. (307.4,50.4) ;
            	\draw (211,259) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (381.5,259) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\draw (212,35) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\draw (249,259) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            	\draw (299.5,259) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            	\draw (215.5,192.5) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            	\draw (214.5,51.5) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            	\draw (236,109) node [anchor=north west][inner sep=0.75pt]    {$y=%s^{x}$};
            \end{tikzpicture} \end{center}''' %(x1,x2,k,base**x2,base))

            # Nội dung câu hỏi
            noidungcauhoi = (
                r'''Diện tích hình phẳng gạch sọc trong hình vẽ bên dưới bằng %s''' % tikz_code
            )

            # Các đáp án
            # Đáp án đúng: tích phân từ x1 đến x2 của (base^x - k)
            da_dung = "\\int_{%s}^{%s} (%s^x - %s) dx" % (x1, x2, base, k)

            # Đáp án sai
            s_wrong = [
                "\\int_{%s}^{%s} (%s^x + %s) dx" % (x1, x2, base, k),
                "\\int_{%s}^{%s} (%s - %s^x) dx" % (x1, x2, k, base),
                "\\int_{%s}^{%s} %s^x dx" % (x1, x2, base),
                "\\int_{%s}^{%s} (%s^x - %s) dx" % (x1, x2, base, x1) # Sai hằng số
            ]

            # Đảm bảo đáp án không trùng
            wrong_answers = [item for item in s_wrong if item != da_dung]
            selected_wrongs = random.sample(wrong_answers, 3)

            # Đưa các đáp án vào danh sách
            list_1 = ["\\True $%s$" % da_dung, "$%s$" % selected_wrongs[0], "$%s$" % selected_wrongs[1], "$%s$" % selected_wrongs[2]]
            random.shuffle(list_1)

            # Lời giải
            loigiai = (
                "Hình phẳng gạch sọc trong hình vẽ được giới hạn bởi các đường $y = %s^x$, $y = %s$, $x = %s$ và $x = %s$. \\\\"
                "Do đó diện tích hình phẳng gạch sọc trong hình vẽ bằng $\\int_{%s}^{%s} |%s^x - %s| \\text{d}x = \\int_{%s}^{%s} (%s^x - %s) \\text{d}x$." % 
                (base, k, x1, x2, x1, x2, base, k, x1, x2, base, k)
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

