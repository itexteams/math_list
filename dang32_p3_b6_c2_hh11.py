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


def bt_dang32_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            # Các biến số: h (chiều cao AA'), d1 (đường chéo AC), d2 (đường chéo BD)
            h_val = random.randint(3, 8)
            d1_val = random.randint(2, 6)
            d2_val = random.randint(1, 4)

            # Tính toán diện tích đáy và thể tích (Dùng float để làm tròn thập phân)
            s_day = 0.5 * d1_val * d2_val
            v_num = s_day * h_val

            # Hàm định dạng số: Làm tròn 1 chữ số thập phân, thay dấu chấm bằng dấu phẩy
            def format_num(val):
                rounded_val = round(float(val), 1)
                # Chuyển sang chuỗi với 1 chữ số thập phân
                s = "{:.1f}".format(rounded_val)
                # Nếu là .0 và bạn muốn viết gọn thành số nguyên thì có thể xử lý thêm, 
                # nhưng theo yêu cầu "hàng phần chục" nên giữ lại .1f
                return s.replace('.', ',')

            kq_dung = '$V = %s$' % format_num(v_num)

            # Bước 4: Các phương án sai
            s_list = [
                '$V = %s$' % format_num(v_num * 2),
                '$V = %s$' % format_num(v_num / 2),
                '$V = %s$' % format_num(v_num * 2 / 3),
                '$V = %s$' % format_num(v_num + 2.5),
                '$V = %s$' % format_num(v_num + 1.2),
                '$V = %s$' % format_num(v_num / 3)
            ]

            # Loại bỏ các đáp án bị trùng với đáp án đúng
            s_list = [x for x in s_list if x != kq_dung]
            random.shuffle(s_list)

            da_s1 = s_list[0]
            da_s2 = s_list[1]
            da_s3 = s_list[2]

            # Nội dung câu hỏi (Đã bỏ ký tự a)
            noidungcauhoi = ('Cho hình lăng trụ đứng $ABCD.A\'B\'C\'D\'$ có đáy là hình thoi, biết $AA\' = %s$, $AC = %s$, $BD = %s$. Thể tích $V$ của khối lăng trụ bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười).'
                             % (format_num(h_val), format_num(d1_val), format_num(d2_val)))

            # Vẽ hình TikZ
            tikz_code = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (92.47,168.4) -- (212.47,168.4) ;
            		\draw [line width=1]    (92.47,68.4) -- (212.47,68.4) ;
            		\draw [line width=1]    (92.47,168.4) -- (92.47,68.4) ;
            		\draw [line width=1]    (212.47,168.4) -- (212.47,68.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (132.47,28.4) ;
            		\draw [line width=1]    (252.47,128.4) -- (252.47,28.4) ;
            		\draw [line width=1]    (132.47,28.4) -- (252.47,28.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (252.47,128.4) ;
            		\draw [line width=1]    (92.47,68.4) -- (132.47,28.4) ;
            		\draw [line width=1]    (212.47,68.4) -- (252.47,28.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (132.47,128.4) ;
            		\draw [line width=1]    (212.47,168.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (212.47,168.4) ;
            		\draw (73,53) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (124,6) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (255,13) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (212.47,68.4) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (75,166) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            		\draw (110,112) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            		\draw (256,115) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            		\draw (212.47,168.4) node [anchor=north west][inner sep=0.75pt]    {$D'$};
            	\end{tikzpicture}
            \end{center}'''
            )

            # Lời giải chi tiết (Đã bỏ ký tự a)
            loigiai = ('Diện tích đáy $ABCD$ là hình thoi nên: $S_{ABCD} = \\frac{1}{2} \\cdot AC \\cdot BD = \\frac{1}{2} \\cdot %s \\cdot %s = %s$. \\\\\n'
                       'Chiều cao của lăng trụ đứng là $h = AA\' = %s$. \\\\\n'
                       'Thể tích $V$ của khối lăng trụ là: $V = S_{ABCD} \\cdot AA\' = \\left( \\frac{1}{2} \\cdot AC \\cdot BD \\right) \\cdot AA\' = \\frac{1}{2} \\cdot %s \\cdot %s \\cdot %s = %s$.'
                       % (format_num(d1_val), format_num(d2_val), format_num(s_day), 
                          format_num(h_val), format_num(d1_val), format_num(d2_val), format_num(h_val), format_num(v_num)))

            # Đáp án ngắn (Sử dụng format_num cho kqz)
            dapan = '\\shortans[0]{$%s$}\n' % format_num(v_num)
            # Trộn đáp án
            da_d = '\\True ' + kq_dung
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

