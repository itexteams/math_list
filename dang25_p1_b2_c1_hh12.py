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


def bt_dang25_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tọa độ điểm P
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 4)

        kq_num = a + b + c
        kq = str(kq_num)

        # Mã TikZ (tuyệt đối KHÔNG gán lệnh replace vào chuỗi này để bảo toàn lệnh -- của TikZ)
        tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8, x={(-0.5cm,-0.4cm)}, y={(1cm,0cm)}, z={(0cm,1cm)}]
        \\draw[->] (0,0,0) -- (5,0,0) node[below] {$x$};
        \\draw[->] (0,0,0) -- (0,5,0) node[below] {$y$};
        \\draw[->] (0,0,0) -- (0,0,5) node[left] {$z$};
        \\node[below right] at (0,0,0) {$O$};
        \\foreach \\i in {1,2,3,4} {
            \\draw (\\i,-0.1,0) -- (\\i,0.1,0) node[above right] {$\\i$};
            \\draw (-0.1,\\i,0) -- (0.1,\\i,0) node[below right] {$\\i$};
            \\draw (-0.1,0,\\i) -- (0.1,0,\\i) node[left] {$\\i$};  }
        \\foreach \\i in {1,2,3,4} {
            \\draw[gray, thin] (\\i,0,0) -- (\\i,4,0);
            \\draw[gray, thin] (0,\\i,0) -- (4,\\i,0);
            \\draw[gray, thin] (0,\\i,0) -- (0,\\i,4);
            \\draw[gray, thin] (0,0,\\i) -- (0,4,\\i);
            \\draw[gray, thin] (\\i,0,0) -- (\\i,0,4);
            \\draw[gray, thin] (0,0,\\i) -- (4,0,\\i);  }
        \\coordinate (P) at (%s,%s,%s);
        \\fill (P) circle (1.5pt) node[right] {$P$};
        \\draw[red, thick] (P) -- (%s,%s,0);
        \\draw[red, thick] (P) -- (0,%s,%s);
        \\draw[red, thick] (P) -- (%s,0,%s);
        \\fill (%s,%s,0) circle (1.5pt);
        \\fill (0,%s,%s) circle (1.5pt);
        \\fill (%s,0,%s) circle (1.5pt);
    \\end{tikzpicture}
    \\end{center}''' % (a,b,c, a,b, b,c, a,c, a,b, b,c, a,c))

        # Các đáp án trắc nghiệm
        du = ['$%s$'%(kq)]
        da= random.choice(du)

        s = ['$%s$'%(kq_num+1),
             '$%s$'%(kq_num+2),
             '$%s$'%(kq_num+3),
             '$%s$'%(abs(kq_num-1)),
             '$%s$'%(abs(kq_num-2)),
             '$%s$'%(abs(kq_num-3))
            ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Xử lý text câu hỏi (Chỉ áp dụng replace dấu vào phần chữ)
        cau_hoi_text = '''Biết điểm $P(a;b;c)$, tính $a+b+c$.'''
        cau_hoi_text = cau_hoi_text.replace('+-', '-').replace('--', '+')

        # Ghép TikZ và câu hỏi lại với nhau
        noidungcauhoi = ('''Trong không gian $Oxyz$, cho điểm $P$ được biểu diễn trong hình vẽ dưới đây:\n%s\n%s''' % (tikz, cau_hoi_text))

        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải (Chỉ áp dụng replace dấu vào lời giải)
        loigiai_text = ('''Từ hình vẽ, ta xác định được hình chiếu của điểm $P$ lên các trục $Ox, Oy, Oz$ lần lượt có tọa độ là $x=%s, y=%s, z=%s$.\\\\
    Suy ra tọa độ điểm $P(%s;%s;%s) \\longrightarrow a=%s; b=%s; c=%s \\longrightarrow a+b+c=%s$.''' % (a, b, c, a, b, c, a, b, c, kq))
        loigiai = loigiai_text.replace('+-', '-').replace('--', '+')

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

