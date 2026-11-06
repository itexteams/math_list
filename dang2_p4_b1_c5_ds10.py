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


def bt_dang2_p4_b1_c5_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                ab=randint(5,30)
                bc=randint(5,30)
                cd=randint(5,30)
                da=randint(5,30)
                ae=randint(5,30)
                be=randint(5,30)
                ce=randint(5,30)
                de=randint(5,30)
                tong=ab+bc+cd+da+ae+be+ce+de
                t1=bc+cd+da+ae+be
                t2=ab+cd+da+be+ce
                t3=ab+bc+da+ce+de
                t4=ab+bc+cd+ae+de
                h1=min(t1,t2,t3,t4)
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                '''Một trò chơi điện tử quy định như sau: Có $5$ trụ $A, B,C, D, E$ với số
                                lượng các thử thách trên đường đi giữa các cặp trụ được mô tả trong
                                hình bên. Người chơi xuất phát từ một trụ nào đó, đi qua tất cả các
                                trụ còn lại, mỗi khi đi qua một trụ thì trụ đó sẽ bị phá hủy và không
                                thể quay trở lại trụ đó được nữa, nhưng người chơi vẫn phải trở về
                                trụ ban đầu. Tìm tổng số thử thách của đường đi thoả mãn điều kiện
                                trên nhận giá trị nhỏ nhất.'''
                                '}{'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                    '\\clip(-0.5968577354938456,-0.6929904665384333) rectangle (5.863740290468574,4.929365410485814); \n'
                                    '\\draw [line width=1.pt] (3.,4.)-- (0.,3.); \n'
                                    '\\draw [line width=1.pt] (0.,3.)-- (1.,0.); \n'
                                    '\\draw [line width=1.pt] (1.,0.)-- (4.943718419682786,0.); \n'
                                    '\\draw [line width=1.pt] (4.943718419682786,0.)-- (3.,4.); \n'
                                    '\\draw [line width=1.pt] (3.,4.)-- (2.4392144380992535,2.0057403544332053); \n'
                                    '\\draw [line width=1.pt] (2.4392144380992535,2.0057403544332053)-- (0.,3.); \n'
                                    '\\draw [line width=1.pt] (2.4392144380992535,2.0057403544332053)-- (1.,0.); \n'
                                    '\\draw [line width=1.pt] (2.4392144380992535,2.0057403544332053)-- (4.943718419682786,0.); \n'
                                    '\\draw (2.899225373492147,4.622691453557218) node[anchor=north west] {$A$}; \n'
                                    '\\draw (-0.6,3.3551057649190246) node[anchor=north west] {$B$}; \n'
                                    '\\draw (0.7218402792991168,0.04302703009019536) node[anchor=north west] {$C$}; \n'
                                    '\\draw (4.943718419682786,0.12480675193782077) node[anchor=north west] {$D$}; \n'
                                    '\\draw (2.6232188122564106,2.394194033209426) node[anchor=north west] {$E$}; \n'
                                    '\\draw (1.2738534017705894,4.0809007963167) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (0,1.5661743495022187) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.807223186413568,-0.018307761295523698) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (3.93169436181842,2.680423059676115) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.807223186413568,3.1813238559928205) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (0.9160671186872275,2.506641150749911) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (1.825866524242062,1.0857184836474194) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (3,1.177720670725998) node[anchor=north west] {$%s$}; \n'
                                '\\end{tikzpicture}  \n'
                                '}'
                                %(latex(ab),latex(bc),latex(cd),latex(da),latex(ae),latex(be),latex(ce),latex(de)
                                ))

                # Nội dung lời giải
                loigiai = ('Mỗi cách đi thỏa mãn yêu cầu bài toán là một hình gồm $5$ cạnh khép kín trong $8$ cạnh được tạo ra bỏ đi ba cạnh trong đó gồm một cạnh là cạnh của tứ giác $ABCD$ và hai cạnh nối từ điểm $E$ đến hai đỉnh còn lại. \\\\ \n'
                        'Tổng số thử thách trên $8$ đường đi là \\\\ \n'
                        '\\hspace*{1cm} $%s+%s+%s+%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AB$ và $CE, DE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $BC$ và $DE, AE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $CD$ và $AE, BE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $DA$ và $BE, CE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Vậy tổng số thử thách nhỏ nhất là $%s$.'


                        %(latex(ab),latex(bc),latex(cd),latex(da),latex(ae),latex(be),latex(ce),latex(de),latex(tong),
                            latex(tong),latex(ab),latex(ce),latex(de),latex(t1),
                            latex(tong),latex(bc),latex(de),latex(ae),latex(t2),
                            latex(tong),latex(cd),latex(ae),latex(be),latex(t3),
                            latex(tong),latex(da),latex(be),latex(ce),latex(t4),
                            latex(kq)
                            ))


            if dang=='1':
                ab=randint(5,30)
                bc=randint(5,30)
                cd=randint(5,30)
                da=randint(5,30)
                ae=randint(5,30)
                be=randint(5,30)
                ce=randint(5,30)
                de=randint(5,30)
                tong=ab+bc+cd+da+ae+be+ce+de
                t1=bc+cd+da+ae+be
                t2=ab+cd+da+be+ce
                t3=ab+bc+da+ce+de
                t4=ab+bc+cd+ae+de
                h1=max(t1,t2,t3,t4)
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                '''Một trò chơi điện tử quy định như sau: Có $5$ trụ $A, B,C, D, E$ với số
                                lượng các thử thách trên đường đi giữa các cặp trụ được mô tả trong
                                hình bên. Người chơi xuất phát từ một trụ nào đó, đi qua tất cả các
                                trụ còn lại, mỗi khi đi qua một trụ thì trụ đó sẽ bị phá hủy và không
                                thể quay trở lại trụ đó được nữa, nhưng người chơi vẫn phải trở về
                                trụ ban đầu. Tìm tổng số thử thách của đường đi thoả mãn điều kiện
                                trên nhận giá trị lớn nhất.'''
                                '}{'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                    '\\clip(-0.5968577354938456,-0.6929904665384333) rectangle (5.863740290468574,4.929365410485814); \n'
                                    '\\draw [line width=1.pt] (3.,4.)-- (0.,3.); \n'
                                    '\\draw [line width=1.pt] (0.,3.)-- (1.,0.); \n'
                                    '\\draw [line width=1.pt] (1.,0.)-- (4.943718419682786,0.); \n'
                                    '\\draw [line width=1.pt] (4.943718419682786,0.)-- (3.,4.); \n'
                                    '\\draw [line width=1.pt] (3.,4.)-- (2.4392144380992535,2.0057403544332053); \n'
                                    '\\draw [line width=1.pt] (2.4392144380992535,2.0057403544332053)-- (0.,3.); \n'
                                    '\\draw [line width=1.pt] (2.4392144380992535,2.0057403544332053)-- (1.,0.); \n'
                                    '\\draw [line width=1.pt] (2.4392144380992535,2.0057403544332053)-- (4.943718419682786,0.); \n'
                                    '\\draw (2.899225373492147,4.622691453557218) node[anchor=north west] {$A$}; \n'
                                    '\\draw (-0.6,3.3551057649190246) node[anchor=north west] {$B$}; \n'
                                    '\\draw (0.7218402792991168,0.04302703009019536) node[anchor=north west] {$C$}; \n'
                                    '\\draw (4.943718419682786,0.12480675193782077) node[anchor=north west] {$D$}; \n'
                                    '\\draw (2.6232188122564106,2.394194033209426) node[anchor=north west] {$E$}; \n'
                                    '\\draw (1.2738534017705894,4.0809007963167) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (0,1.5661743495022187) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.807223186413568,-0.018307761295523698) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (3.93169436181842,2.680423059676115) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.807223186413568,3.1813238559928205) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (0.9160671186872275,2.506641150749911) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (1.825866524242062,1.0857184836474194) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (3,1.177720670725998) node[anchor=north west] {$%s$}; \n'
                                '\\end{tikzpicture}  \n'
                                '}'
                                %(latex(ab),latex(bc),latex(cd),latex(da),latex(ae),latex(be),latex(ce),latex(de)
                                ))

                # Nội dung lời giải
                loigiai = ('Mỗi cách đi thỏa mãn yêu cầu bài toán là một hình gồm $5$ cạnh khép kín trong $8$ cạnh được tạo ra bỏ đi ba cạnh trong đó gồm một cạnh là cạnh của tứ giác $ABCD$ và hai cạnh nối từ điểm $E$ đến hai đỉnh còn lại. \\\\ \n'
                        'Tổng số thử thách trên $8$ đường đi là \\\\ \n'
                        '\\hspace*{1cm} $%s+%s+%s+%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AB$ và $CE, DE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $BC$ và $DE, AE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $CD$ và $AE, BE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $DA$ và $BE, CE$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s-%s=%s$. \\\\ \n'
                        'Vậy tổng số thử thách lớn nhất là $%s$.'


                        %(latex(ab),latex(bc),latex(cd),latex(da),latex(ae),latex(be),latex(ce),latex(de),latex(tong),
                            latex(tong),latex(ab),latex(ce),latex(de),latex(t1),
                            latex(tong),latex(bc),latex(de),latex(ae),latex(t2),
                            latex(tong),latex(cd),latex(ae),latex(be),latex(t3),
                            latex(tong),latex(da),latex(be),latex(ce),latex(t4),
                            latex(kq)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content                   

