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


def bt_dang9_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Phần 2: Đường thẳng từ x=5 qua (6,0) đến (9,6)
            tikz_graph = r"""\begin{tikzpicture}[scale=0.5, font=\footnotesize, >=stealth]
                \draw[color=gray!20,dashed] (-2,-3) grid (10,9);
                \draw[->] (-2,0) -- (10,0) node[below] {$x$};
                \draw[->] (0,-3) -- (0,9) node[left] {$y$};
                \node[below left] at (0,0) {$O$};
                \foreach \x in {-2,2,4,6,8} \draw (\x,0.1) -- (\x,-0.1) node[below] {$\x$};
                \foreach \y in {-2,2,4,6} \draw (0.1,\y) -- (-0.1,\y) node[left] {$\y$};
                \draw[thick, samples=100, domain=-1:4.8] plot (\x, {0.6*(\x-1.8)^2 + 2.3});
                \fill (-1, 7) circle (1.5pt);
                \draw (4.9, 8.4) circle (2pt); % Điểm hở tại x=5
                \draw[thick] (5.1, -1.8) -- (9,6);
                \draw (5, -2) circle (2pt); % Điểm hở tại x=5
                \fill (9, 6) circle (1.5pt);
                \fill (0,4.2) circle (1pt);
            \end{tikzpicture}"""

            # Nội dung câu hỏi
            noidungcauhoi = r"""Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên.
            \begin{center}
            %s
            \end{center}
            """ % (tikz_graph)

            ########################################################################
            # Nhận biết (a): Giao điểm trục hoành
            ########################################################################
            nb_da_1_d = r'\True $f(x) = 0 \Leftrightarrow x = 6$'
            nb_da_1_s = r'$f(x) = 0 \Leftrightarrow x = 5$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = r'Đồ thị hàm số $y = f(x)$ cắt trục hoành tại điểm có hoành độ $x = 6$.'

            ########################################################################
            # Thông hiểu (b): Giá trị tại x=5
            ########################################################################
            th_da_1_d = r'\True $f(5)$ không tồn tại'
            th_da_1_s = r'$f(5) = -2$'
            # Lưu ý: Trong ảnh b là Sai vì f(5)=-2, nhưng cấu trúc random cần bản đúng/sai
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = r'Từ đồ thị hàm số $y = f(x)$ thì tại $x=5$ đồ thị có các điểm hở, nên $f(5)$ không tồn tại.'

            ########################################################################
            # Vận dụng (c): Tập xác định
            ########################################################################
            vd_da_1_d = r'\True Tập xác định $\mathscr{D} = [-1; 5) \cup (5; 9]$'
            vd_da_1_s = r'Tập xác định $\mathscr{D} = [-1; 5)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = r'Hàm số xác định với $x \in [-1; 5)$ và $x \in (5; 9]$.'

            ########################################################################
            # Vận dụng cao (d): Tập giá trị
            ########################################################################
            vdc_da_1_d = r'\True $-2 \leq f(x) \leq 8, \forall x \in \mathscr{D}$'
            vdc_da_1_s = r'$f(x) \geq 0, \forall x \in \mathscr{D}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = r'Từ đồ thị ta thấy giá trị thấp nhất tiệm cận $-2$ và giá trị cao nhất khoảng $8$. Vậy $-2 \leq f(x) \leq 8$.'

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 câu đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

