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


def bt_dang94_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo tính ngẫu nhiên cho bài toán
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Hàm gốc của đề bài: y = 1 + sin|x|
                da_text = 'y = 1 + \\sin |x|'
                s_funcs = ['y = 1 + \\sin |x|.', 'y = |\\sin x|', 'y = 1 + |\\cos x|', 'y = 1 - \\sin |x|', 'y = |\\cos x|']
                # Loại bỏ chính hàm đúng ra khỏi danh sách nhiễu
                if 'y = 1 + \\sin |x|.' in s_funcs: s_funcs.remove('y = 1 + \\sin |x|.')
                random.shuffle(s_funcs)
                das1, das2, das3 = s_funcs[0], s_funcs[1], s_funcs[2]

                # TikZ vẽ đồ thị y = 1 + sin|x| nét 1pt
                tikz_graph = '\\draw[line width=1pt,smooth,samples=200,domain=-11:11] plot(\\x,{1+abs(sin(\\x*180/3.14159))});'

                noidungcauhoi = ('''Đường cong trong hình dưới đây là đồ thị của một hàm số trong bốn hàm số được liệt kê ở bốn phương án $A, B, C, D$? Hỏi hàm số đó là hàm số nào?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.5, >=stealth]
                \\draw[color=gray!30,line width=0.5pt] (-11.5,-0.5) grid (11.5,3.5);
                \\draw[->,line width=1pt] (-11.5,0) -- (11.5,0) node[above] {$x$};
                \\draw[->,line width=1pt] (0,-0.8) -- (0,3.8) node[right] {$y$};
                \\node[below left] at (0,0) {$O$};
                %s
                \\filldraw (0,1) circle (2pt) node[below right] {$1$};
                \\filldraw (0,2) circle (2pt) node[right] {$2$};
                \\filldraw (3.14159,0) circle (1.5pt) node[below] {$\\pi$};
                \\filldraw (6.28318,0) circle (1.5pt) node[below] {$2\\pi$};
                \\filldraw (9.42477,0) circle (1.5pt) node[below] {$3\\pi$};
                \\filldraw (-3.14159,0) circle (1.5pt) node[below left] {$-\\pi$};
                \\filldraw (-6.28318,0) circle (1.5pt) node[below] {$-2\\pi$};
                \\filldraw (-9.42477,0) circle (1.5pt) node[below] {$-3\\pi$};
            \\end{tikzpicture}
            \\end{center}''' % (tikz_graph))

                loigiai = ('''Ta có đồ thị đi qua điểm $(0;1)$, thay $x = 0$ vào bốn phương án:\\\\
            - Với $y = 1 + |\\cos x|$, tại $x = 0 \\Rightarrow y = 2$ nên bị loại.\\\\
            - Với $y = |\\sin x|$, tại $x = 0 \\Rightarrow y = 0$ nên bị loại.\\\\
            Xét tại $x = \\frac{\\pi}{2}$, nhìn vào đồ thị ta thấy $y = 2$. Thay vào phương án còn lại chỉ có $%s$ thỏa mãn.''' % (da_text))

            else:
                # Hàm biến đổi ngẫu nhiên: y = 1 + |cos x|
                da_text = 'y = 1 + |\\cos x|'
                s_funcs = ['y = 1 + \\sin |x|', 'y = |\\sin x|', 'y = 1 + \\sin x', 'y = 1 - \\cos x', 'y = |\\cos x|']
                random.shuffle(s_funcs)
                das1, das2, das3 = s_funcs[0], s_funcs[1], s_funcs[2]

                # TikZ vẽ đồ thị y = 1 + |cos x| nét 1pt
                tikz_graph = '\\draw[line width=1pt,smooth,samples=200,domain=-11:11] plot(\\x,{1+abs(cos(\\x*180/3.14159))});'

                noidungcauhoi = ('''Đường cong trong hình dưới đây là đồ thị của một hàm số trong bốn hàm số được liệt kê ở bốn phương án $A, B, C, D$? Hỏi hàm số đó là hàm số nào?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.5, >=stealth]
                \\draw[color=gray!30,line width=0.5pt] (-11.5,-0.5) grid (11.5,3.5);
                \\draw[->,line width=1pt] (-11.5,0) -- (11.5,0) node[above] {$x$};
                \\draw[->,line width=1pt] (0,-0.8) -- (0,3.8) node[right] {$y$};
                \\node[below left] at (0,0) {$O$};
                %s
                \\filldraw (0,2) circle (2pt) node[above left] {$2$};
                \\filldraw (0,1) circle (2pt) node[left] {$1$};
                \\filldraw (1.5708,0) circle (1.5pt) node[below] {$\\frac{\\pi}{2}$};
                \\filldraw (4.7124,0) circle (1.5pt) node[below] {$\\frac{3\\pi}{2}$};
                \\filldraw (-1.5708,0) circle (1.5pt) node[below] {$-\\frac{\\pi}{2}$};
            \\end{tikzpicture}
            \\end{center}''' % (tikz_graph))

                loigiai = ('''Ta có đồ thị đi qua điểm $(0;2)$, thay $x = 0$ vào bốn phương án chỉ có $%s$ cho kết quả $y = 2$. Do đó hàm số thỏa mãn đề bài là $%s$.''' % (da_text, da_text))

            # Định dạng các phương án trắc nghiệm đảm bảo tuyệt đối không có dấu chấm ở cuối
            da_d = ('\\True $' + str(da_text) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Trộn thứ tự ngẫu nhiên của bốn phương án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Định dạng xuất mã câu hỏi trắc nghiệm theo minipage mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

