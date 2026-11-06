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


def bt_dang91_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng đồ thị ngẫu nhiên
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Đồ thị gốc: y = cos(x) + 1
                da_text = 'y = \\cos x + 1'
                s_funcs = ['y = 2 - \\sin x', 'y = 2\\cos x', 'y = \\cos^2 x + 1', 'y = \\sin x + 1', 'y = \\cos x - 1']
                random.shuffle(s_funcs)
                das1, das2, das3 = s_funcs[0], s_funcs[1], s_funcs[2]

                tikz_plot = '\\draw[line width=1pt,color=blue,smooth,samples=100,domain=-4.5:4.5] plot(\\x,{cos(\\x*180/3.14159)+1});'

                noidungcauhoi = ('''Đường cong trong hình vẽ bên dưới là đồ thị của một trong bốn hàm số được liệt kê ở bốn phương án A, B, C, D dưới đây. Hỏi hàm số đó là hàm số nào?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.7, >=stealth]
                \\draw[->,line width=1pt] (-5,0) -- (5,0) node[below] {$x$};
                \\draw[->,line width=1pt] (0,-2.5) -- (0,3) node[right] {$y$};
                \\node[below left] at (0,0) {$O$};
                %s
                \\filldraw[red] (-3.14159,0) circle (1.5pt) node[below] {$-\\pi$};
                \\filldraw[red] (3.14159,0) circle (1.5pt) node[below] {$\\pi$};
                \\filldraw[red] (0,2) circle (1.5pt) node[above left] {$2$};
                \\filldraw[red] (-1.5708,1) circle (1.5pt);
                \\node[below left] at (-1.5708,0) {$-\\frac{\\pi}{2}$};
                \\draw[dashed,line width=0.5pt] (-1.5708,0) -- (-1.5708,1);
                \\filldraw[red] (1.5708,1) circle (1.5pt);
                \\node[below] at (1.5708,0) {$\\frac{\\pi}{2}$};
                \\draw[dashed,line width=0.5pt] (1.5708,0) -- (1.5708,1);
                \\draw[line width=0.5pt] (-0.1,1) -- (0.1,1) node[left=2pt] {$1$};
                \\draw[line width=0.5pt] (-0.1,-1) -- (0.1,-1) node[left=2pt] {$-1$};
                \\draw[line width=0.5pt] (-0.1,-2) -- (0.1,-2) node[left=2pt] {$-2$};
            \\end{tikzpicture}
            \\end{center}''' % (tikz_plot))

                loigiai = ('''Do đồ thị đi qua ba điểm $(-\\pi;0)$, $(0;2)$, $(\\pi;0)$ nên chọn phương án $%s$.''' % (da_text))

            else:
                # Đồ thị dạng 2: y = 1 - cos(x)
                da_text = 'y = 1 - \\cos x'
                s_funcs = ['y = \\sin x + 1', 'y = 1 + \\cos x', 'y = 2\\sin x', 'y = \\sin^2 x + 1', 'y = \\cos x - 1']
                random.shuffle(s_funcs)
                das1, das2, das3 = s_funcs[0], s_funcs[1], s_funcs[2]

                tikz_plot = '\\draw[line width=1pt,color=blue,smooth,samples=100,domain=-4.5:4.5] plot(\\x,{1-cos(\\x*180/3.14159)});'

                noidungcauhoi = ('''Đường cong trong hình vẽ bên dưới là đồ thị của một trong bốn hàm số được liệt kê ở bốn phương án A, B, C, D dưới đây. Hỏi hàm số đó là hàm số nào?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.7, >=stealth]
                \\draw[->,line width=1pt] (-5,0) -- (5,0) node[below] {$x$};
                \\draw[->,line width=1pt] (0,-1.5) -- (0,3.5) node[right] {$y$};
                \\node[below left] at (0,0) {$O$};
                %s
                \\filldraw[red] (-3.14159,2) circle (1.5pt);
                \\node[below] at (-3.14159,0) {$-\\pi$};
                \\draw[dashed,line width=0.5pt] (-3.14159,0) -- (-3.14159,2);
                \\filldraw[red] (3.14159,2) circle (1.5pt);
                \\node[below] at (3.14159,0) {$\\pi$};
                \\draw[dashed,line width=0.5pt] (3.14159,0) -- (3.14159,2);
                \\filldraw[red] (0,0) circle (1.5pt);
                \\filldraw[red] (-1.5708,1) circle (1.5pt);
                \\node[below left] at (-1.5708,0) {$-\\frac{\\pi}{2}$};
                \\draw[dashed,line width=0.5pt] (-1.5708,0) -- (-1.5708,1);
                \\filldraw[red] (1.5708,1) circle (1.5pt);
                \\node[below] at (1.5708,0) {$\\frac{\\pi}{2}$};
                \\draw[dashed,line width=0.5pt] (1.5708,0) -- (1.5708,1);
                \\draw[line width=0.5pt] (-0.1,1) -- (0.1,1) node[left=2pt] {$1$};
                \\draw[line width=0.5pt] (-0.1,2) -- (0.1,2) node[left=2pt] {$2$};
                \\draw[line width=0.5pt] (-0.1,-1) -- (0.1,-1) node[left=2pt] {$-1$};
            \\end{tikzpicture}
            \\end{center}''' % (tikz_plot))

                loigiai = ('''Do đồ thị đi qua ba điểm $(-\\pi;2)$, $(0;0)$, $(\\pi;2)$ nên chọn phương án $%s$.''' % (da_text))

            # Định dạng các phương án trắc nghiệm không chứa dấu chấm ở cuối
            da_d = ('\\True $' + str(da_text) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Trộn ngẫu nhiên các phương án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm định dạng mẫu minipage
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

