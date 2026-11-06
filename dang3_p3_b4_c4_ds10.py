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


def bt_dang3_p3_b4_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                k=randint(1,9)
                a=4*k
                b=9*k
                c=5*k
                d=4*k
                f1=sqrt(x**2+a**2)/d
                f2=(b-x)/c
                f3=c**2*(x**2+a**2)
                f4=d**2*(b-x)**2
                f=(d**2-c**2)*x**2-2*b*d**2*x+b**2*d**2-a**2*c**2
                hsa=d**2-c**2
                hsb=-2*b*d**2
                hsc=b**2*d**2-a**2*c**2
                delta=hsb**2-4*hsa*hsc
                x1=(-hsb-sqrt(delta))/(2*hsa)
                x2=(-hsb+sqrt(delta))/(2*hsa)
                h1=x1    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Bác Việt sống và làm việc tại trạm hải đăng cách bờ biển $%s$ kmzz Hằng tuần bác chèo thuyền vào vị trí gần nhất trên bờ biển là bến Bính để nhận hàng hóa do cơ quan cung cấpzz Tuần này, do trục trặc về vận chuyển nên toàn bộ số hàng vẫn đang nằm ở thôn Hoành, bên bờ biển cách bến Bính $%s$ km và sẽ được anh Nam vận chuyển trên con đường dọc bờ biển tới bến Bính bằng xe kéozz Bác Việt đã gọi điện thống nhất với anh Nam là họ sẽ gặp nhau ở vị trí nào đó giữa bến Bính và thôn Hoành để hai người có mặt tại đó cùng lúc, không mất thời gian chờ nhauzz Hai người gặp nhau cách bến Bính bao nhiêu? (làm tròn hết quả đến hàng phần chục), biết rằng vận tốc kéo xe của anh Nam là $%s$ km/h và thuyền của bác Việt di chuyển với vận tốc $%s$ km/hzz Ngoài ra giả thiết rằng đường bờ biển từ thôn Hoành đến bến Bính là đường thẳng và bác Việt cũng luôn chèo thuyền tới một điểm trên bờ biển theo một đường thẳngzz \n'
                                %(latex(a),latex(b),latex(c),latex(d)
                                ))

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\definecolor{qqqqff}{rgb}{0zz,0zz,1zz}
                \\definecolor{ffqqqq}{rgb}{1zz,0zz,0zz}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1zz2126107177707848,-1zz0435416020489232) rectangle (7zz254681834536318,3zz382543141202517);
                    \\draw [line width=1zzpt ,color=ffqqqq] (-1zz,0zz)-- (7zz,0zz);
                    \\draw [line width=1zzpt ] (0zz,0zz)-- (0zz,3zz);
                    \\draw [line width=1zzpt ,color=qqqqff] (0zz,3zz)-- (2zz,0zz);
                    \\draw [->,line width=1zzpt ] (3zz5,-0zz5) -- (7zz,-0zz5);
                    \\draw [->,line width=1zzpt ] (3zz5,-0zz5) -- (0zz,-0zz5);
                    \\draw (-0zz5,3zz5) node[anchor=north west] {$A$};
                    \\draw (-0zz4,0zz05763407078899538) node[anchor=north west] {$B$};
                    \\draw (6zz6,0zz06832509673887809) node[anchor=north west] {$C$};
                    \\draw (1zz7,0zz07901612268876079) node[anchor=north west] {$M$};
                    \\draw (0zz7759201089073984,0zz49596613473418627) node[anchor=north west] {$x$};
                    \\draw (-1zz4,1zz7575071968203455) node[anchor=north west] {$%s$ km};
                    \\draw (3zz07449068813218,-0zz4448441488554918) node[anchor=north west] {$%s$ km};
                \\end{tikzpicture}
            \\end{center} Ta mô hình hóa bài toán như hình vẽ: Tramh hải đăng ở vị trí $A$; bến Bính ở $B$ và thôn Hoành ở $C$zz Giả sử bác Việt chèo thuyền cập bến ở vị trí $M$ và ta đặt $BM=x, (x>0)$zz Để hai người không phải chờ nhau thì thời gian chèo thuyền bằng thời gian kéo xe nên ta có phương trình:\\\\
                        $$%s=%szz$$
                        Bình phương hai vế ta có phương trình \\\\ 
                        $%s=%s$ hay $%s=0$zz\\\\ 
                        Giải phương trình ta được $x=%s$ và $x=%s$ (loại)zz \\\\
                        Vậy vị trí hai người gặp nhau cách bên Bính $%s$ kmzz'''


                        %(latex(a),latex(b),
                            latex(f1),latex(f2),
                            latex(f3),latex(f4),latex(f),
                            latex(x1),latex(x2),latex(kq),

                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content

