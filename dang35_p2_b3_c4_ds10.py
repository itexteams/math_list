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


def bt_dang35_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Random các thông số cơ bản
            # Giữ nguyên cấu trúc x1=2, x2=6 như đề bài hoặc có thể random nhẹ
            x1 = 2
            x2 = 6
            k_val = random.randint(1, 3) # Random hệ số k dương

            # Tính toán m và n dựa trên k, x1, x2
            # f(x) = k(x - x1)(x - x2) = kx^2 - k(x1+x2)x + k*x1*x2
            # So sánh với f(x) = kx^2 - mx + n
            m_val = k_val * (x1 + x2)
            n_val = k_val * (x1 * x2)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Tam thức bậc hai $f(x) = %sx^2 - %sx + %s$ có bảng xét dấu như hình vẽ:
            \begin{center}
            \begin{tikzpicture}
            \tkzTabInit[espcl=1.5,lgt=1.5]{$x$/1,$f(x)$/1}{$-\infty$,$%s$,$%s$,$+\infty$}
            \tkzTabLine{,+,0,-,0,+,}
            \end{tikzpicture}
            \end{center}
            Xét tính đúng, sai của các khẳng định sau:''' % (
                latex(k_val) if k_val != 1 else "", 
                latex(m_val), 
                latex(n_val),
                latex(x1),
                latex(x2)
            )

            ########################################################################
            # a) Tập nghiệm f(x) < 0
            a_da_d = r'\True Bất phương trình $f(x) < 0$ có tập nghiệm là $(%s; %s)$' % (latex(x1), latex(x2))
            a_da_s = r'Bất phương trình $f(x) < 0$ có tập nghiệm là $(-\infty; %s) \cup (%s; +\infty)$' % (latex(x1), latex(x2))
            list_a = [a_da_d, a_da_s]
            ans_a = random.choice(list_a)
            loigiai_a = r'''Dựa vào bảng xét dấu, ta thấy $f(x)$ mang dấu âm trong khoảng giữa hai nghiệm. Vậy tập nghiệm của $f(x) < 0$ là $(%s; %s)$.''' % (latex(x1), latex(x2))

            ########################################################################
            # b) Bất phương trình (x^2 + 4)f(x) > 0
            b_da_d = r'\True Bất phương trình $(x^2 + 4)f(x) > 0$ có tập nghiệm gồm 2 khoảng rời nhau'
            b_da_s = r'Bất phương trình $(x^2 + 4)f(x) > 0$ có tập nghiệm là một khoảng duy nhất'
            list_b = [b_da_d, b_da_s]
            ans_b = random.choice(list_b)
            loigiai_b = r'''Vì $x^2 + 4 > 0$ với mọi $x \in \mathbb{R}$, nên $(x^2 + 4)f(x) > 0 \Leftrightarrow f(x) > 0$. 
            Dựa vào bảng xét dấu, $f(x) > 0 \Leftrightarrow x \in (-\infty; %s) \cup (%s; +\infty)$. 
            Tập nghiệm gồm 2 khoảng rời nhau.''' % (latex(x1), latex(x2))

            ########################################################################
            # c) Biểu thức m + n
            val_c = m_val + n_val
            ratio_c = Rational(val_c, k_val)
            c_da_d = r'\True $m + n = %sk$' % (latex(ratio_c))
            c_da_s = r'$m + n = %sk$' % (latex(ratio_c + 2))
            list_c = [c_da_d, c_da_s]
            ans_c = random.choice(list_c)
            loigiai_c = r'''Ta có $m = %s$ và $n = %s$. Suy ra $m + n = %s + %s = %s$. 
            Mà $13k = 13 \cdot %s = %s$. Do đó $m + n = %sk$.''' % (
                latex(m_val), latex(n_val), latex(m_val), latex(n_val), latex(val_c), 
                latex(k_val), latex(13*k_val), latex(ratio_c)
            )

            ########################################################################
            # d) Bất phương trình f(sqrt(x)) <= 12k
            # f(sqrt(x)) = kx - m*sqrt(x) + n <= 12k
            # Đặt t = sqrt(x), t >= 0. Giải bpt: kt^2 - mt + n - 12k <= 0
            # Với k=1, m=8, n=12: t^2 - 8t + 12 - 12 <= 0 <=> t^2 - 8t <= 0 <=> 0 <= t <= 8
            # => 0 <= x <= 64. Số chính phương: 0, 1, 4, 9, 16, 25, 36, 49, 64 (9 nghiệm)
            t = symbols('t')
            f_t = k_val*t**2 - m_val*t + n_val - 12*k_val
            sol_t = solve(f_t <= 0, t)
            # Giả sử điều kiện chuẩn là x >= 0, ta lấy phần giao với t >= 0
            t_max = 8 # Với bộ số 2, 6 thì t_max luôn là 8
            num_cp = 9 # Các số 0, 1, 4, 9, 16, 25, 36, 49, 64

            d_da_d = r'\True Bất phương trình $f(\sqrt{x}) \le 12k$ có $%s$ nghiệm là số chính phương' % (num_cp)
            d_da_s = r'Bất phương trình $f(\sqrt{x}) \le 12k$ có $%s$ nghiệm là số chính phương' % (num_cp+1)
            list_d = [d_da_d, d_da_s]
            ans_d = random.choice(list_d)

            loigiai_d = r'''Điều kiện: $x \ge 0$. Đặt $t = \sqrt{x}$ ($t \ge 0$). \\
            Bất phương trình trở thành: $kt^2 - mt + n \le 12k \Leftrightarrow %st^2 - %st + %s \le %s$ \\
            $\Leftrightarrow %st^2 - %st \le 0 \Leftrightarrow 0 \le t \le 8$. \\
            Suy ra $0 \le \sqrt{x} \le 8 \Leftrightarrow 0 \le x \le 64$. \\
            Các số chính phương trong đoạn $[0; 64]$ là $\{0, 1, 4, 9, 16, 25, 36, 49, 64\}$. Có %s nghiệm.''' % (
                latex(k_val) if k_val != 1 else "", latex(m_val), latex(n_val), latex(12*k_val),
                latex(k_val) if k_val != 1 else "", latex(m_val), num_cp
            )

            # Tổng hợp và xuất nội dung (Không dùng tiền tố r trong biến content cuối)
            # Lưu ý: Các biến ans_x và loigiai_x đã được xử lý chuỗi.
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

