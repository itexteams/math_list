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


def bt_dang9_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':

        # Ngẫu nhiên hệ số nhân k để tạo các bài toán khác nhau
        k = randint(2, 6)

        # Các đáp án trắc nghiệm
        du = ['$T = %s$' % (latex(k)),
              ]
        da= random.choice(du)
        s = ['$T = %s$' % (latex(k + 1)),
             '$T = %s$' % (latex(k + 2)),
             '$T = %s$' % (latex(k + 3)),
             '$T = %s$' % (latex(2 * k)),
             '$T = \\frac{1}{%s}$' % (latex(k)),
             '$T = 0$',
            ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABC$. Bên trong tam giác $ABC$ ta lấy một điểm $O$ bất kỳ. Từ $O$ ta dựng các đường thẳng lần lượt song song với $SA, SB, SC$ và cắt các mặt phẳng $(SBC), (SCA), (SAB)$ theo thứ tự tại $A', B', C'$. Khi đó giá trị $T = %s \\cdot \\left(\\frac{OA'}{SA} + \\frac{OB'}{SB} + \\frac{OC'}{SC}\\right)$ bằng bao nhiêu?'''
                         %(latex(k))
                         )
        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải
        loigiai=('''\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (2.5,-1.2);
        \\coordinate (C) at (5.5,0);
        \\coordinate (S) at (2,4);
        \\coordinate (M) at (3.85,-0.66);
        \\coordinate (N) at (1.27,0);
        \\coordinate (P) at (0.67,-0.32);
        \\coordinate (O) at (1.54,-0.26);
        \\coordinate (A') at (2.74,2.14);
        \\coordinate (B') at (1.43,0.88);
        \\coordinate (C') at (0.91,0.46);
        \\draw[line width=1pt] (S)--(A) (S)--(B) (S)--(C) (A)--(B)--(C) (S)--(M);
        \\draw[line width=1pt, dashed] (A)--(C) (A)--(M) (B)--(N) (C)--(P) (S)--(N) (S)--(P) (O)--(A') (O)--(B') (O)--(C');
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[below] {$B$};
        \\fill (C) circle (1pt) node[right] {$C$};
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (M) circle (1pt) node[below right] {$M$};
        \\fill (N) circle (1pt) node[above] {$N$};
        \\fill (P) circle (1pt) node[left] {$P$};
        \\fill (O) circle (1pt) node[below left] {$O$};
        \\fill (A') circle (1pt) node[right] {$A'$};
        \\fill (B') circle (1pt) node[left] {$B'$};
        \\fill (C') circle (1pt) node[left] {$C'$};
        \\coordinate (A2) at (8,3);
        \\coordinate (B2) at (6,0);
        \\coordinate (C2) at (11,0);
        \\coordinate (M2) at (8.2,0);
        \\coordinate (O2) at (8,1);
        \\coordinate (N2) at (9.33,1.67);
        \\coordinate (P2) at (6.91,1.36);
        \\draw[line width=1pt] (A2)--(B2)--(C2)--cycle (A2)--(M2) (B2)--(N2) (C2)--(P2);
        \\fill (A2) circle (1pt) node[above] {$A$};
        \\fill (B2) circle (1pt) node[left] {$B$};
        \\fill (C2) circle (1pt) node[right] {$C$};
        \\fill (M2) circle (1pt) node[below] {$M$};
        \\fill (N2) circle (1pt) node[right] {$N$};
        \\fill (P2) circle (1pt) node[left] {$P$};
        \\fill (O2) circle (1pt) node[below left] {$O$};
        \\end{tikzpicture}
        \\end{center} Gọi $M, N, P$ lần lượt là giao điểm của $AO$ và $BC$, $BO$ và $AC$, $CO$ và $AB$.\\\\
    Ta có:\\\\
    $\\frac{OA'}{SA} = \\frac{MO}{MA} = \\frac{S_{CMO}}{S_{CMA}} = \\frac{S_{BMO}}{S_{BMA}} = \\frac{S_{CMO} + S_{BMO}}{S_{CMA} + S_{BMA}} = \\frac{S_{OBC}}{S_{ABC}}$\\\\
    $\\frac{OB'}{SB} = \\frac{NO}{NB} = \\frac{S_{ANO}}{S_{ANB}} = \\frac{S_{CNO}}{S_{CNB}} = \\frac{S_{ANO} + S_{CNO}}{S_{ANB} + S_{CNB}} = \\frac{S_{OAC}}{S_{ABC}}$\\\\
    $\\frac{OC'}{SC} = \\frac{PO}{PC} = \\frac{S_{APO}}{S_{APC}} = \\frac{S_{BPO}}{S_{BPC}} = \\frac{S_{APO} + S_{BPO}}{S_{APC} + S_{BPC}} = \\frac{S_{OAB}}{S_{ABC}}$\\\\
    Từ đó suy ra:\\\\
    $\\frac{OA'}{SA} + \\frac{OB'}{SB} + \\frac{OC'}{SC} = \\frac{S_{OBC} + S_{OAC} + S_{OAB}}{S_{ABC}} = \\frac{S_{ABC}}{S_{ABC}} = 1$\\\\
    Khi đó giá trị biểu thức $T$ bằng:\\\\
    $T = %s \\cdot 1 = %s$.'''
                 %(latex(k),latex(k))
                 )
    dapan='\\shortans[0]{$%s$}\n'%(latex(k))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-')
    return content 

