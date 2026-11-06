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


def bt_dang23_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Danh sách các bộ đỉnh để hoán vị
            vertex_sets = [
                ('A', 'B', 'C', 'D'),
                ('S', 'A', 'B', 'C'),
                ('M', 'N', 'P', 'Q'),
            ]

            # Chọn ngẫu nhiên một bộ đỉnh
            v = random.choice(vertex_sets)
            v1, v2, v3, v4 = v[0], v[1], v[2], v[3]

            # Trong bài toán này, cạnh chung của 2 tam giác đều là v1v2
            # M là trung điểm của v1v2
            m_label = 'M' 

            # Bước 4: Điều chỉnh các phương án không trùng lặp
            da_dung = '$%s%s \\perp \\left(%s%s%s\\right)$' % (v1, v2, m_label, v3, v4)

            # Các phương án sai
            da_sai1 = '$%s%s \\perp \\left(%s%s%s\\right)$' % (v3, m_label, v1, v2, v4)
            da_sai2 = '$%s%s \\perp \\left(%s%s%s\\right)$' % (v1, v2, v2, v3, v4)
            da_sai3 = '$%s%s \\perp \\left(%s%s%s\\right)$' % (v4, m_label, v1, v2, v3)

            # Đảm bảo các phương án sai không trùng đáp án đúng (logic hình học đảm bảo điều này)
            list_da = [('\\True ' + da_dung), da_sai1, da_sai2, da_sai3]
            random.shuffle(list_da)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$ có hai mặt $%s%s%s$ và $%s%s%s$ là hai tam giác đều. Gọi $%s$ là trung điểm của $%s%s$. Khẳng định nào sau đây đúng?'''
                             % (v1, v2, v3, v4, v1, v2, v3, v1, v2, v4, m_label, v1, v2))

            # Hình vẽ TikZ
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=1.2]
                \\coordinate (M) at (0,0);
                \\coordinate (A) at (-1.5,-0.3);
                \\coordinate (B) at (1.5,0.3);
                \\coordinate (C) at (2,-1.2);
                \\coordinate (D) at (0,2.5);
                \\draw[dashed] (A) -- (B);
                \\draw (A) -- (C);
                \\draw[dashed] (C) -- (M);
                \\draw (D) -- (A);
                \\draw (D) -- (B);
                \\draw (D) -- (C);
                \\draw[dashed] (D) -- (M);
                \\draw (B) -- (C);
                \\fill (A)  node[left]{$%s$};
                \\fill (B) node[right]{$%s$};
                \\fill (C) node[right]{$%s$};
                \\fill (D) node[above]{$%s$};
                \\fill (M) node[below left]{$%s$};
            \\end{tikzpicture}
            \\end{center}''' % (v1, v2, v3, v4, m_label))

            # Lời giải chi tiết
            loigiai = ('''Vì tam giác $%s%s%s$ là tam giác đều và $%s$ là trung điểm của $%s%s$ nên $%s%s \\perp %s%s$ (đường trung tuyến đồng thời là đường cao). \\\\
            Vì tam giác $%s%s%s$ là tam giác đều và $%s$ là trung điểm của $%s%s$ nên $%s%s \\perp %s%s$ (đường trung tuyến đồng thời là đường cao). \\\\
            Ta có:
            $\\left\\{ \\begin{array}{l} %s%s \\perp %s%s \\\\ %s%s \\perp %s%s \\end{array} \\right. \\Rightarrow %s%s \\perp \\left(%s%s%s\\right)$.'''
                       % (v1, v2, v3, m_label, v1, v2, v3, m_label, v1, v2,
                          v1, v2, v4, m_label, v1, v2, v4, m_label, v1, v2,
                          v3, m_label, v1, v2, v4, m_label, v1, v2, v1, v2, m_label, v3, v4))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + tikz_code + '\n'
                       '\\choice \n'
                       '{' + str(list_da[0]) + '}\n'
                       '{' + str(list_da[1]) + '}\n'
                       '{' + str(list_da[2]) + '}\n'
                       '{' + str(list_da[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

