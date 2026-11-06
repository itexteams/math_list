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


def bt_dang25_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số của cạnh a
                list_he_so = [1, 2, 3, 4, 5, 10]
                k = random.choice(list_he_so)

                if k == 1:
                    canh_a = 'a'
                else:
                    canh_a = f'{k}a'

                # Đáp án đúng luôn là 90 độ
                da_dung = '90^\\circ'

                # Các đáp án sai
                s = ['30^\\circ', '45^\\circ', '60^\\circ']
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$ cạnh $%s$. Gọi $M$ là trung điểm của $CD$ và $N$ là trung điểm của $A'D'$. Tính góc giữa hai đường thẳng $B'M$ và $C'N$.'''
                                 %(canh_a))

                # Các đáp án trắc nghiệm
                da_d = ('\\True $' + da_dung + '$')
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải với TikZ
                loigiai = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,4);
                \\coordinate (B) at (4,4);
                \\coordinate (C) at (5,5);
                \\coordinate (D) at (1,5);
                \\coordinate (A1) at (0,0);
                \\coordinate (B1) at (4,0);
                \\coordinate (C1) at (5,1.5);
                \\coordinate (D1) at (1,1.5);
                \\coordinate (M) at ($(C)!0.5!(D)$);
                \\coordinate (N) at ($(A1)!0.5!(D1)$);
                \\coordinate (I) at ($(C1)!0.5!(D1)$);
                \\draw (A)--(B)--(C)--(D)--cycle;
                \\draw (A)--(A1) (B)--(B1) (C)--(C1);
                \\draw (A1)--(B1)--(C1);
                \\draw[dashed] (D)--(D1) (D1)--(A1) (D1)--(C1);
                \\draw[dashed] (B1)--(M);
                \\draw[dashed] (C1)--(N);
                \\draw[dashed] (B1)--(I) (M)--(I);
                \\draw (A) node[left]{$A$} (B) node[right]{$B$} (C) node[right]{$C$} (D) node[left]{$D$};
                \\draw (A1) node[left]{$A'$} (B1) node[right]{$B'$} (C1) node[right]{$C'$} (D1) node[left]{$D'$};
                \\draw (M) node[above]{$M$} (N) node[below]{$N$} (I) node[below]{$I$};
            \\end{tikzpicture}
            \\end{center}
            Gọi $I$ là trung điểm của $C'D'$. \\\\
            Vì $MI \\parallel CC'$ và $CC' \\perp (A'B'C'D')$ nên $MI \\perp (A'B'C'D')$. \\\\
            Suy ra $IB'$ là hình chiếu vuông góc của $B'M$ trên mặt phẳng $(A'B'C'D')$. \\\\
            Xét hình vuông $A'B'C'D'$, ta có $\\triangle B'C'I = \\triangle C'D'N$ (hai cạnh góc vuông tương ứng bằng $a$ và $\\frac{a}{2}$). \\\\
            Do đó $\\widehat{IB'C'} = \\widehat{NC'D'}$. \\\\
            Mặt khác ta có $\\widehat{IB'C'} + \\widehat{IC'B'} = 90^\\circ \\Rightarrow \\widehat{NC'D'} + \\widehat{IC'B'} = 90^\\circ$. \\\\
            Suy ra $C'N \\perp IB'$. \\\\
            Theo định lý ba đường vuông góc, vì $C'N \\perp IB'$ nên $C'N \\perp B'M$. \\\\
            Vậy góc giữa $B'M$ và $C'N$ bằng $90^\\circ$.''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

