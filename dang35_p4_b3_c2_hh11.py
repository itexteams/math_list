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


def bt_dang35_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lis_params = [
                {'a_coeff': 1, 'bb_sqrt': 3, 'angle': 30}, # AB=a, BB'=a*sqrt(3) -> tan = 1/sqrt(3) -> 30 deg
                {'a_coeff': 1, 'bb_sqrt': 1, 'angle': 45}, # AB=a, BB'=a -> tan = 1 -> 45 deg
                {'a_coeff': 3, 'bb_sqrt': 1, 'angle': 60, 'a_is_sqrt': True}, # AB=a*sqrt(3), BB'=a -> tan = sqrt(3) -> 60 deg
            ]

            param = random.choice(lis_params)
            n = random.randint(1, 5) # Hệ số nhân để random độ dài cạnh

            # Thiết lập giá trị AB và BB'
            # Giả sử cạnh cơ sở là 'a'
            if param.get('a_is_sqrt'):
                ab_text = latex(n) + 'a\\sqrt{3}'
                ab_val_expr = n * sqrt(3)
            else:
                ab_text = latex(n) + 'a' if n > 1 else 'a'
                ab_val_expr = n

            bb_val = n * sqrt(param['bb_sqrt'])
            bb_text = latex(n) + 'a' if param['bb_sqrt'] == 1 else (latex(n) + 'a\\sqrt{3}' if n > 1 else 'a\\sqrt{3}')

            # Đáp án đúng
            kq_angle = param['angle']
            da_d = '$'+str(kq_angle) + '^{\\circ}$'

            # Các đáp án sai
            s = ['$30^{\\circ}$', '$45^{\\circ}$', '$60^{\\circ}$', '$90^{\\circ}$']
            if da_d in s:
                s.remove(da_d)
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Câu hỏi
            noidungcauhoi = ('''Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác vuông tại $B$, $AB = BC = %s$, $BB' = %s$. Tính góc giữa đường thẳng $A'B$ và mặt phẳng $\\left(BCC'B'\\right)$.'''
                              % (ab_text, bb_text))

            # Hình vẽ TikZ
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[line cap=round,line join=round, x=1.0cm,y=1.0cm, line width=1pt, scale=0.8]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.5,-1.2);
                \coordinate (C) at (4,0);
                \coordinate (A1) at (0,4);
                \coordinate (B1) at (1.5,2.8);
                \coordinate (C1) at (4,4);
                \draw [dashed] (A)--(C);
                \draw (A)--(B)--(C);
                \draw (A1)--(B1)--(C1)--cycle;
                \draw (A)--(A1) (B)--(B1) (C)--(C1);
                \draw (A1)--(B);
                \draw[fill=black] (A) circle (1pt) node[left] {$A$};
                \draw[fill=black] (B) circle (1pt) node[below] {$B$};
                \draw[fill=black] (C) circle (1pt) node[right] {$C$};
                \draw[fill=black] (A1) circle (1pt) node[left] {$A'$};
                \draw[fill=black] (B1) circle (1pt) node[right] {$B'$};
                \draw[fill=black] (C1) circle (1pt) node[right] {$C'$};
            \end{tikzpicture}
            \end{center}'''

            # Lời giải chi tiết
            loigiai = ('''Hình lăng trụ đứng $ABC.A'B'C'$ nên $BB' \\perp \\left(A'B'C'\\right) \\Rightarrow BB' \\perp A'B' \\Rightarrow A'B' \\perp BB'$ (1).\\\\
            Bài ra có $AB \\perp BC \\Rightarrow A'B' \\perp B'C'$.\\\\
            Kết hợp với (1) $\\Rightarrow A'B' \\perp \\left(BCC'B'\\right) \\Rightarrow$ Hình chiếu của $A'B$ trên mặt phẳng $\\left(BCC'B'\\right)$ là $B'B$.\\\\
            Do đó $\\left(A'B; \\left(BCC'B'\\right)\\right) = \\widehat{A'BB'}$.\\\\
            Xét tam giác vuông $A'B'B$ tại $B'$, ta có:\\\\
            $\\tan \\widehat{A'BB'} = \\frac{A'B'}{BB'} = \\frac{%s}{%s} = %s$.\\\\
            Suy ra $\\widehat{A'BB'} =$ %s.'''
                        % (ab_text, bb_text, latex(simplify(ab_val_expr/bb_val)), da_d))

            # Trộn đáp án
            list_ans = ['\\True ' + da_d, das1, das2, das3]
            random.shuffle(list_ans)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

