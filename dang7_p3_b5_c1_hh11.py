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


def bt_dang7_p3_b5_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    # Hình vẽ TikZ chuẩn theo yêu cầu: màu black, nét 1pt, điểm 1pt
    hinh_ve = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, color=black] (-0.3,-0.5) -- (5.2,-0.5) -- (4.2,-3.2) -- (-1.3,-3.2) -- cycle;
        \\node[color=black] at (4.4,-0.9) {$(ABC)$};
        \\coordinate (A) at (0,-2);
        \\coordinate (B) at (1.8,-2.7);
        \\coordinate (C) at (4.1,-1.9);
        \\coordinate (D) at (1.1,0.8);
        \\coordinate (E) at (2.9,0.1);
        \\coordinate (F) at (5.2,0.9);
        \\draw[line width=1pt, dashed, ->, color=black] (5.1,1.7) -- (5.7,0.4);
        \\node[above, color=black] at (5.5,1.6) {Phương chiếu};
        \\draw[line width=1pt, ->, color=black] (D) -- (A);
        \\draw[line width=1pt, ->, color=black] (E) -- (B);
        \\draw[line width=1pt, ->, color=black] (F) -- (C);
        \\draw[line width=1pt, color=black] (D) -- (E) -- (F) -- cycle;
        \\draw[line width=1pt, color=black] (A) -- (B) -- (C) -- cycle;
        \\fill[color=black] (A) circle (1pt) node[left] {$A$};
        \\fill[color=black] (B) circle (1pt) node[below] {$B$};
        \\fill[color=black] (C) circle (1pt) node[right] {$C$};
        \\fill[color=black] (D) circle (1pt) node[above left] {$D$};
        \\fill[color=black] (E) circle (1pt) node[above] {$E$};
        \\fill[color=black] (F) circle (1pt) node[above right] {$F$};
    \\end{tikzpicture}
    \\end{center}'''

    if dang == '1':
        # Chiếu theo phương AD lên mặt phẳng (ABC)
        kq_str = '3'

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho lăng trụ tam giác $ABC.DEF$ có $AD // BE // CF$. Chiếu song song sáu đỉnh của lăng trụ lên mặt phẳng $(ABC)$ theo phương $AD$. Hỏi sáu đỉnh đó có tất cả bao nhiêu hình chiếu phân biệt? \\\\
    %s''' % (hinh_ve))

        # Nội dung lời giải
        loigiai = ('''Ba điểm $A,B,C$ nằm ngay trên mặt phẳng chiếu $(ABC)$ nên hình chiếu của chúng lần lượt là chính $A,B,C$. \\\\
                   Vì $AD // BE // CF$ và phương chiếu là phương $AD$, nên đường chiếu qua $D$ đi qua $A$; đường chiếu qua $E$ đi qua $B$; đường chiếu qua $F$ đi qua $C$. Do đó $D\\mapsto A, E\\mapsto B, F\\mapsto C$. \\\\
                   Sáu đỉnh chỉ cho ba hình chiếu phân biệt là $A,B,C$.''')

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    elif dang == '2':
        # Chiếu theo phương AD lên mặt phẳng đáy còn lại (DEF)
        kq_str = '3'

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho lăng trụ tam giác $ABC.DEF$ có $AD // BE // CF$. Chiếu song song sáu đỉnh của lăng trụ lên mặt phẳng $(DEF)$ theo phương $AD$. Hỏi sáu đỉnh đó có tất cả bao nhiêu hình chiếu phân biệt? \\\\
    %s''' % (hinh_ve))

        # Nội dung lời giải
        loigiai = ('''Ba điểm $D,E,F$ nằm ngay trên mặt phẳng chiếu $(DEF)$ nên hình chiếu của chúng lần lượt là chính $D,E,F$. \\\\
                   Vì $AD // BE // CF$ và phương chiếu là phương $AD$, nên đường chiếu qua $A$ đi qua $D$; đường chiếu qua $B$ đi qua $E$; đường chiếu qua $C$ đi qua $F$. Do đó $A\\mapsto D, B\\mapsto E, C\\mapsto F$. \\\\
                   Sáu đỉnh chỉ cho ba hình chiếu phân biệt là $D,E,F$.''')

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

