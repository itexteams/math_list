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


def bt_dang10_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Gọi tỉ lệ SD = x * GD. Chọn ngẫu nhiên x từ 2 đến 6
        x_val = random.randint(2, 6)

        # Tính tỉ lệ SE/SA = (x-1)/x = p/q
        p = x_val - 1
        q = x_val
        ratio_expr = Rational(p, q)

        # Các đáp án trắc nghiệm
        du = ['$%s$' % latex(x_val)]
        da = du[0]

        # Tạo các phương án sai ngẫu nhiên
        s_list_raw = [x_val + 1, x_val + 2, x_val + 3, abs(x_val - 1) if x_val - 1 > 0 else x_val + 4, x_val * 2]
        s_list = []
        for val in s_list_raw:
            s_list.append('$%s$' % latex(val))

        # Đảm bảo phương án sai không trùng lặp với đáp án đúng
        s_list = list(set(s_list) - set(du))

        das1 = s_list[0]
        das2 = s_list[1]
        das3 = s_list[2]

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang $AD // BC$. Gọi $E$ là điểm thuộc cạnh $SA$ sao cho $\\frac{SE}{SA} = %s$. Mặt phẳng $(BCE)$ cắt $SD$ tại $G$. Biết $SD = x \\cdot GD$. Giá trị của $x$ bằng bao nhiêu?'''
                         % (latex(ratio_expr)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''\\begin{center}
           \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (0,0);
            \\coordinate (D) at (4,0);
            \\coordinate (B) at (0.8,-1.5);
            \\coordinate (C) at (3.2,-1.5);
            \\coordinate (S) at (2,3.5);
            \\coordinate (E) at ($(S)!0.66!(A)$);
            \\coordinate (G) at ($(S)!0.66!(D)$);
            \\draw[line width=1pt] (S)--(A)--(B)--(C)--(D)--(S);
            \\draw[line width=1pt] (S)--(B) (S)--(C) (E)--(B) (G)--(C);
            \\draw[line width=1pt, dashed] (A)--(D) (E)--(G);
            \\fill (A) circle (1pt) node[left] {$A$};
            \\fill (B) circle (1pt) node[below left] {$B$};
            \\fill (C) circle (1pt) node[below right] {$C$};
            \\fill (D) circle (1pt) node[right] {$D$};
            \\fill (S) circle (1pt) node[above] {$S$};
            \\fill (E) circle (1pt) node[left] {$E$};
            \\fill (G) circle (1pt) node[right] {$G$};
           \\end{tikzpicture}
           \\end{center}
           Ta thấy hai mặt phẳng $(SAD)$ và $(BCE)$ lần lượt đi qua hai đường thẳng $AD // BC$ và có $E, G$ là hai điểm chung nên chúng cắt nhau theo giao tuyến $EG // AD // BC$. \\\\
           Lại có vì $EG // AD$ suy ra $\\frac{SE}{SA} = \\frac{SG}{SD} = %s$ nên $SD = %s \\cdot GD$. \\\\
           Vậy $x = %s$.'''
                 % (latex(ratio_expr), latex(x_val), latex(x_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(x_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content 

