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


def bt_dang33_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Các kịch bản random bài toán (chọn các cặp vectơ khác nhau)
            scenarios = [
                {
                    'v1': '\\overrightarrow{BA}', 'v2': '\\overrightarrow{C\'B\'}', 'v3': '\\overrightarrow{CB}',
                    'mid': '180^\\circ - \\widehat{ABC} = 180^\\circ - 60^\\circ', 'ans': '120^\\circ'
                },
                {
                    'v1': '\\overrightarrow{AB}', 'v2': '\\overrightarrow{B\'C\'}', 'v3': '\\overrightarrow{BC}',
                    'mid': '180^\\circ - \\widehat{ABC} = 180^\\circ - 60^\\circ', 'ans': '120^\\circ'
                },
                {
                    'v1': '\\overrightarrow{AB}', 'v2': '\\overrightarrow{A\'C\'}', 'v3': '\\overrightarrow{AC}',
                    'mid': '\\widehat{BAC}', 'ans': '60^\\circ'
                },
                {
                    'v1': '\\overrightarrow{CA}', 'v2': '\\overrightarrow{C\'B\'}', 'v3': '\\overrightarrow{CB}',
                    'mid': '\\widehat{ACB}', 'ans': '60^\\circ'
                }
            ]

            # Random chọn 1 kịch bản
            chosen = random.choice(scenarios)
            vec1 = chosen['v1']
            vec2 = chosen['v2']
            vec3 = chosen['v3']
            step_mid = chosen['mid']
            ans_correct = chosen['ans']

            # Tạo các phương án sai ngẫu nhiên
            all_opts = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ', '120^\\circ', '150^\\circ']
            all_opts.remove(ans_correct)
            wrong_opts = random.sample(all_opts, 3)

            # Các đáp án trắc nghiệm
            da_d = '\\True $%s$' % ans_correct
            da_s1 = '$%s$' % wrong_opts[0]
            da_s2 = '$%s$' % wrong_opts[1]
            da_s3 = '$%s$' % wrong_opts[2]

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Câu hỏi bao gồm hình vẽ TikZ
            noidungcauhoi = ('''Cho lăng trụ đều $ABC.A'B'C'$. Góc giữa hai vectơ $%s$ và $%s$ bằng bao nhiêu?
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\coordinate (A') at (0,0);
            \\coordinate (C') at (3.5,0);
            \\coordinate (B') at (1.5,-1.5);
            \\coordinate (A) at (0,3);
            \\coordinate (C) at (3.5,3);
            \\coordinate (B) at (1.5,1.5);
            \\draw (A) node[left]{$A$} -- (C) node[right]{$C$} -- (B) node[left]{$B$} -- cycle;
            \\draw (A') node[left]{$A'$} -- (B') node[below]{$B'$} -- (C') node[right]{$C'$};
            \\draw (A) -- (A');
            \\draw (B) -- (B');
            \\draw (C) -- (C');
            \\draw[dashed] (A') -- (C');
            \\fill (A) circle (1.5pt) (B) circle (1.5pt) (C) circle (1.5pt) (A') circle (1.5pt) (B') circle (1.5pt) (C') circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}''' % (vec1, vec2))

            # Nội dung lời giải
            loigiai = ('''Ta có $\\left( %s, %s \\right) = \\left( %s, %s \\right) = %s = %s$.''' % (vec1, vec2, vec1, vec3, step_mid, ans_correct))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

