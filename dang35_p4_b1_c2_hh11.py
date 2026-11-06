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


def bt_dang35_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Mặc dù góc không đổi (60 độ), việc random độ dài cạnh 'a' giúp lời giải cụ thể hơn.
            lis_a = [2, 3, 4, 5, 6, 8, 10]
            a_val = random.choice(lis_a)

            # Các đại lượng tính toán
            # AB = BC = AC = a * sqrt(2)
            # OM = ON = MN = (a * sqrt(2)) / 2
            canh_day_latex = latex(a_val) + r'\sqrt{2}'
            canh_tg_deu_latex = r'\frac{' + latex(a_val) + r'\sqrt{2}}{2}'

            # B4: Điều chỉnh phương án sai không trùng đáp án đúng (60 độ)
            list_angles = ['30^\\circ', '45^\\circ', '90^\\circ', '120^\\circ', '150^\\circ']
            wrong_choices = random.sample(list_angles, 3)

            # Đáp án đúng
            da_dung = '60^\\circ'

            # Hình vẽ TikZ
            tikz_code = r'''\begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth]
                \coordinate (O) at (0,0);
                \coordinate (A) at (0,4);
                \coordinate (B) at (4,1.5);
                \coordinate (C) at (2,-1.5);
                \coordinate (M) at ($(B)!0.5!(C)$);
                \coordinate (N) at ($(A)!0.5!(C)$);
                \draw (A)--(O)--(C) (A)--(B)--(C)--cycle;
                \draw (A)--(C) (M)--(N);
                \draw[dashed] (O)--(B) (O)--(M) ;
                \foreach \p/\pos in {O/left, A/above, B/right, C/below, M/right, N/above right}
                    \fill (\p) node[\pos] {$\p$};
            \end{tikzpicture}'''

            # B2: Viết nội dung câu hỏi và lời giải chi tiết
            noidungcauhoi = ('''Cho tứ diện $OABC$ có $OA, OB, OC$ đôi một vuông góc với nhau và $OA = OB = OC = %s$. Gọi $M$ là trung điểm của $BC$. Tính góc giữa hai đường thẳng $OM$ và $AB$.'''
                            %(latex(a_val)))

            da_d = ('\\True $' + da_dung + '$')
            da_s1 = '$' + wrong_choices[0] + '$'
            da_s2 = '$' + wrong_choices[1] + '$'
            da_s3 = '$' + wrong_choices[2] + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            loigiai = ('''Đặt $OA = OB = OC = a = %s$. \\\\
                        Vì $OA, OB, OC$ đôi một vuông góc nên các tam giác $OAB, OBC, OCA$ là các tam giác vuông cân tại $O$. \\\\
                        Suy ra $AB = BC = AC = a\\sqrt{2} = %s$. \\\\
                        Gọi $N$ là trung điểm của $AC$. Trong tam giác $ABC$, $MN$ là đường trung bình nên $MN // AB$ và $MN = \\frac{AB}{2} = %s$. \\\\
                        Do đó, góc giữa hai đường thẳng $OM$ và $AB$ chính là góc giữa hai đường thẳng $OM$ và $MN$. Xét tam giác $OMN$: \\\\
                        $OM$ là đường trung tuyến trong tam giác vuông $OBC \\Rightarrow OM = \\frac{BC}{2} = %s$. \\\\
                        $ON$ là đường trung tuyến trong tam giác vuông $OAC \\Rightarrow ON = \\frac{AC}{2} = %s$. \\\\
                        $MN = %s$ (đã tính ở trên). \\\\
                        Trong tam giác $OMN$ có $ON = OM = MN = %s$ nên $\\triangle OMN$ là tam giác đều. \\\\
                        Suy ra $\\widehat{OMN} = 60^\\circ$. \\\\
                        Vậy $(OM, AB) = (OM, MN) = 60^\\circ$.'''
                        %(latex(a_val), canh_day_latex, canh_tg_deu_latex, canh_tg_deu_latex, canh_tg_deu_latex, canh_tg_deu_latex, canh_tg_deu_latex))

            # Xuất câu trắc nghiệm - Đảm bảo không dùng r'' trong content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' '\\begin{center}\n' + tikz_code + '\n\\end{center}\n' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

