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


def bt_dang15_p3_b1_c2_hh12(self):
            # Khai báo biến
            a = random.randint(15, 30)
            b = random.randint(15, 30)
            c = random.randint(15, 30)

            # Ensure a, b, c are different
            while len({a, b, c}) < 3:
                a = random.randint(15, 30)
                b = random.randint(15, 30)
                c = random.randint(15, 30)

            # Calculate the distance using the formula d = 1 / sqrt(1/a^2 + 1/b^2 + 1/c^2)
            a_sym, b_sym, c_sym = symbols('a b c')
            dist_val = (1 / sp.sqrt(1/a_sym**2 + 1/b_sym**2 + 1/c_sym**2)).subs({a_sym: a, b_sym: b, c_sym: c})
            dist_approx = float(dist_val)
            dist_rounded = Decimal(dist_approx).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq = str(dist_rounded).replace('.', ',')
            kq_latex = latex(round(dist_approx, 1)).replace('.', ',')

            # Generate correct answer and distractors
            da_val = round(dist_approx, 1)
            du = [f'${latex(da_val).replace(".", ",")}$']
            da = random.choice(du)
            s = [round(dist_approx + 0.1, 1),
                 round(dist_approx + 0.2, 1),
                 round(dist_approx - 0.1, 1),
                 round(dist_approx - 0.2, 1),
                 round(dist_approx + 0.3, 1),
                 round(dist_approx - 0.3, 1)]

            das1_val = random.choice(s)
            s.remove(das1_val)
            das2_val = random.choice(s)
            s.remove(das2_val)
            das3_val = random.choice(s)

            das1 = f'${latex(das1_val).replace(".", ",")}$'
            das2 = f'${latex(das2_val).replace(".", ",")}$'
            das3 = f'${latex(das3_val).replace(".", ",")}$'
            da_d = f'\\True {da}'

            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Problem statement
            noidungcauhoi = (
                f'''Trong một trò chơi mô phỏng bắn súng, một người chơi đặt điểm ngắm tại điểm $O$ là giao điểm của $AC$ và $BD$ trong căn phòng hình hộp chữ nhật $ABCD.A'B'C'D'$ có kích thước $AB={latex(a)}$m, $AD={latex(b)}$m, $AA'={latex(c)}$m. Người chơi di chuyển trên đoạn $BD$ có nhiệm vụ bắn trúng một mục tiêu di động trên mặt phẳng $(CB'D')$. Tính khoảng cách ngắn nhất từ điểm ngắm đó đến mục tiêu (làm tròn kết quả đến hàng phần chục).'''
            )

            # Solution explanation
            loigiai = (
                f'''Chọn hệ trục tọa độ $Oxyz$ như hình vẽ.'''
                '''\\begin{center}
                \\scalebox{0.6}{ 
            	\\begin{tikzpicture}[line join=round, line cap=round, >=stealth, thick]
            		\\coordinate (A)  at (2,1);
            		\\coordinate (B)  at (-2,1);
            		\\coordinate (C)  at (0,3);
            		\\coordinate (D)  at (4,3);
            		\\coordinate (A') at (2,-2);
            		\\coordinate (B') at (-2,-2);
            		\\coordinate (C') at (0,0);
            		\\coordinate (D') at (4,0);
            		\\draw (B') -- (A') -- (D') -- (D) -- (C) -- (B) -- cycle;
            		\\draw (B) -- (A) -- (D);
            		\\draw (A) -- (A');
            		\\draw (B) -- (B');
            		\\draw (C) -- (C');
            		\\draw (D') -- (A);
            		\\draw (B) -- (D);
            		\\draw[dashed] (C') -- (D') (C') -- (B') (C') -- (C) (B') -- (D') (B') -- (C)--(D');
            		\\draw[->] (C)  -- ++(0,1) node[left] {$z$};
            		\\draw[->] (B') -- ++(-1,-1) node[left] {$x$};
            		\\draw[->] (D') -- ++(1,0) node[above] {$y$};
            		\\draw (2,1) node[above left] {$A$};
            		\\draw (-2,1) node[left] {$B$};
            		\\draw (0,3.2) node[left] {$C$};
            		\\draw (4,3) node[right] {$D$};
            		\\draw (2,-2) node[right] {$A'$};
            		\\draw (-2,-2) node[left] {$B'$};
            		\\draw (0,0) node[left] {$C'$};
            		\\draw (4,0) node[above right] {$D'$};
            	\\end{tikzpicture}}
            \\end{center}'''
            f'''Ta có $C(0,0,{latex(c)})$, $D'(0,{latex(b)},0), B'({latex(a)},0,0)$ và $C'(0;0;0)$. \\\\
            Mặt phẳng $(CB'D')$ là mặt phẳng đi qua ba điểm này, có phương trình theo đoạn chắn là: \\\\
            $$\\frac{{x}}{{{latex(a)}}} + \\frac{{y}}{{{latex(b)}}} + \\frac{{z}}{{{latex(c)}}} = 1.$$ \\\\
            Do $BD // (B'CD')$ nên $d(BD,(B'CD'))=d(B,(B'CD'))=d(C',(B'CD'))$. \\\\
            Khoảng cách ngắn nhất từ điểm bắn đến mục tiêu chính là khoảng cách từ $BD$ đến mặt phẳng $(B'CD')$, do vậy ta có \\\\
            $d = \\frac{{|\\frac{{0}}{{{latex(a)}}}+\\frac{{0}}{{{latex(b)}}}+\\frac{{0}}{{{latex(c)}}}-1|}}{{\\sqrt{{(\\frac{{1}}{{{latex(a)}}})^2+(\\frac{{1}}{{{latex(b)}}})^2+(\\frac{{1}}{{{latex(c)}}})^2}}}} = \\frac{{1}}{{\\sqrt{{\\frac{{1}}{{{latex(a)}^2}}+\\frac{{1}}{{{latex(b)}^2}}+\\frac{{1}}{{{latex(c)}^2}}}}}} \\approx {kq} $ m.'''
            )
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content  

