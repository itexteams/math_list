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


def bt_dang2_p3_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (giữ cấu trúc mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Ta random bộ tên các đỉnh của tứ diện để tạo sự khác biệt
                labels_sets = [
                    ('A', 'B', 'C', 'D'),
                    ('S', 'A', 'B', 'C'),
                    ('M', 'N', 'P', 'Q'),
                    ('D', 'A', 'B', 'C')
                ]
                selected_labels = random.choice(labels_sets)
                v1, v2, v3, v4 = selected_labels 
                # v1, v2, v3 tạo thành tam giác cân tại v1 (đáy v2v3)
                # v4, v2, v3 tạo thành tam giác cân tại v4 (đáy v2v3)
                # Cần xác định góc giữa v2v3 và v1v4 (luôn là 90 độ)

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                kq_value = 90
                da = '$%s^\\circ$' % kq_value

                wrong_options = ['$30^\\circ$', '$45^\\circ$', '$60^\\circ$', '$120^\\circ$', '$0^\\circ$']
                random.shuffle(wrong_options)
                das1, das2, das3 = wrong_options[:3]

                # Nội dung câu hỏi (B2: Viết lại y hệt bài toán)
                # Sử dụng \left( \right) và $ $ theo yêu cầu
                noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$ có $%s%s = %s%s$ và $%s%s = %s%s$. Góc của hai đường thẳng $%s%s$ và $%s%s$ bằng bao nhiêu?'''
                                 % (v1, v2, v3, v4, v1, v2, v1, v3, v4, v2, v4, v3, v2, v3, v1, v4))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Vẽ hình TikZ giống 100% ảnh (độ dày 1pt, nét đứt AC và AE)
                # Giả định E là trung điểm BC
                ve_hinh = r'''\begin{center} \begin{tikzpicture}[scale=1.2, line width=1pt, font=\footnotesize]
                \coordinate (A) at (0,1);
                \coordinate (B) at (1.5,-0.5);
                \coordinate (C) at (3.5,1);
                \coordinate (D) at (1.8,3.5);
                \coordinate (E) at ($(B)!0.5!(C)$);
                \draw (D)--(A);
                \draw (D)--(B);
                \draw (D)--(C);
                \draw (A)--(B);
                \draw (B)--(C);
                \draw (D)--(E);
                \draw[dashed] (A)--(C);
                \draw[dashed] (A)--(E);
                \node[left] at (A) {$''' + v1 + r'''$};
                \node[below] at (B) {$''' + v2 + r'''$};
                \node[right] at (C) {$''' + v3 + r'''$};
                \node[above] at (D) {$''' + v4 + r'''$};
                \node[below right] at (E) {$E$};
            \end{tikzpicture} \end{center}'''

                # Nội dung lời giải (B2: Viết chi tiết, không viết tắt)
                loigiai = ('''Gọi $E$ là trung điểm đoạn $%s%s$. \\\\
            Vì $\\triangle %s%s%s$ cân tại $%s$ có $%sE$ là đường trung tuyến nên $%sE \\perp %s%s$. (1) \\\\
            Tương tự, $\\triangle %s%s%s$ cân tại $%s$ có $%sE$ là đường trung tuyến nên $%sE \\perp %s%s$. (2) \\\\
            Từ (1) và (2) suy ra $%s%s \\perp \\left(%s%sE\\right)$, mà $%s%s \\subset \\left(%s%sE\\right)$ nên $%s%s \\perp %s%s$. \\\\
            Vậy góc giữa hai đường thẳng $%s%s$ và $%s%s$ bằng $90^\\circ$.'''
                           % (v2, v3, v1, v2, v3, v1, v1, v1, v2, v3,
                              v4, v2, v3, v4, v4, v4, v2, v3,
                              v2, v3, v1, v4, v1, v4, v1, v4, v2, v3, v1, v4,
                              v2, v3, v1, v4))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(90)
            # Xuất câu trắc nghiệm (không dùng raw string r'' ở content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' +str(ve_hinh)+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content         

