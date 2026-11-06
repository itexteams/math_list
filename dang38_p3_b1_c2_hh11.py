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


def bt_dang38_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo danh sách các biến số để random
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random tên biến độ dài (a, b, x, k...)
                bien_ten = random.choice(['a', 'x', 'm', 'k', 'b'])
                a = symbols(bien_ten)

                # Bước 4: Điều chỉnh các phương án sai
                # Đáp án đúng là 60 độ
                kq_dung = '60^\\circ'

                # Danh sách các phương án nhiễu
                ds_nhieu = ['30^\\circ', '45^\\circ', '90^\\circ', '120^\\circ']
                random.shuffle(ds_nhieu)

                das1 = ds_nhieu[0]
                das2 = ds_nhieu[1]
                das3 = ds_nhieu[2]

                # Nội dung câu hỏi
                # Sử dụng biến đã chọn để thay thế cho 'a' trong hình ảnh
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $SA = SB = SC = AB = AC = %s$, $BC = %s\\sqrt{2}$. Góc giữa hai đường thẳng $AB$ và $SC$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 %(latex(a), latex(a)))

                # Vẽ hình bằng TikZ (Chuyển đổi từ hình ảnh sang code)
                hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (1.5,-2);
                \\coordinate (C) at (4.5,0);
                \\coordinate (H) at ($(B)!0.5!(C)$);
                \\coordinate (S) at ($(H)+(0,4)$);
                \\coordinate (M) at ($(S)!0.5!(A)$);
                \\coordinate (N) at ($(S)!0.5!(B)$);
                \\draw (S)--(A) (S)--(B) (S)--(C) (A)--(B) (B)--(C) (S)--(H) (M)--(N) (N)--(H);
                \\draw[dashed] (A)--(C)  (A)--(H) (M)--(H) ;
                \\draw (H)++(-0.2,0.1) -- ++(0.1,0.2) -- ++(0.2,-0.1);
                \\fill (S)  node[above] {$S$};
                \\fill (A)  node[left] {$A$};
                \\fill (B)  node[below] {$B$};
                \\fill (C)  node[right] {$C$};
                \\fill (H)  node[below right] {$H$};
                \\fill (M)  node[left] {$M$};
                \\fill (N)  node[right] {$N$};
            \\end{tikzpicture}
            \\end{center}''')

                # Các đáp án
                da_d = ('\\True $' + str(kq_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết dựa theo ảnh
                loigiai = ('''Gọi $H$ là hình chiếu vuông góc của $S$ lên mặt phẳng $(ABC)$. \\\\
                          Theo giả thiết $SA = SB = SC$ nên $H$ là tâm đường tròn ngoại tiếp tam giác $ABC$. \\\\
                          Xét tam giác $ABC$ có $AB = AC = %s$ và $BC = %s\\sqrt{2}$. \\\\
                          Ta thấy $AB^2 + AC^2 = %s^2 + %s^2 = 2%s^2 = BC^2$, suy ra tam giác $ABC$ vuông cân tại $A$. \\\\
                          Do đó $H$ là trung điểm của $BC$. \\\\
                          Gọi $M, N$ lần lượt là trung điểm của $SA, SB$. Khi đó: \\\\
                          $\\begin{cases} MN \\parallel AB \\\\ HN \\parallel SC \\end{cases} \\Rightarrow$ Góc giữa $AB$ và $SC$ là góc giữa $MN$ và $HN$. \\\\
                          Xét tam giác $\\triangle MNH$ ta có: \\\\
                          $MN = \\frac{AB}{2} = \\frac{%s}{2}$. \\\\
                          $HN = \\frac{SC}{2} = \\frac{%s}{2}$. \\\\
                          $MH = \\frac{SA}{2} = \\frac{%s}{2}$ (Do $\\triangle SHA$ vuông tại $H$, $MH$ là đường trung tuyến ứng với cạnh huyền $SA$). \\\\
                          $\\Rightarrow$ Tam giác $\\triangle MNH$ là tam giác đều $\\Rightarrow \\widehat{MNH} = 60^\\circ$. \\\\
                          Vậy góc cần tìm là $60^\\circ$.'''
                          %(latex(a), latex(a), latex(a), latex(a), latex(a), 
                            latex(a), latex(a), latex(a)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(60))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(hinh_ve)+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

