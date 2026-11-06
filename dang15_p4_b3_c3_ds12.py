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


def bt_dang15_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a1=randint(1,12)
                a=a1*10
                b=nsimplify(a/2)
                h=b-1
                d=nsimplify(b/2)
                g=nsimplify((-4*h)/(3*b**2))*x**3+h*x
                k1=g.subs(x,b/2)
                k2=g.subs(x,-b/2)
                s=nsimplify(a**2-4*(k1-k2))
                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Một hoa văn trang trí được tạo ra từ một miếng bìa mỏng hình vuông cạnh bằng $%s$ cm bằng cách khoét đi bốn phần bằng nhau có hình dạng parabol như hình bên. '
                                'Biết $AB=%s$ cm, $IH=%s$ cm. Tính diện tích bề mặt hoa văn đó.'
                            '}{'
                            '\\scalebox{0.6}{ '  
                            '\\begin{tikzpicture}[scale=0.6]\n'
                            '\\draw[dashed,red] (5,2)--(5,-2);\n'
                            '\\draw[dashed,red] (1,0)--(5,0);\n'
                            '\\node at (5,2) [right]{$A$};\n'
                            '\\node at (5,-2) [right]{$B$};\n'
                            '\\node at (5,0) [right]{$H$};\n'
                            '\\draw[samples=500]\n'
                'plot[domain=-5:-1](\\x,{sqrt(-\\x-1)})\n'
                'plot[domain=-5:-1](\\x,{-sqrt(-\\x-1)})\n'
                'plot[domain=1:5](\\x,{sqrt(\\x-1)})\n'
                'plot[domain=1:5](\\x,{-sqrt(\\x-1)})\n'
                'plot[domain=-2:2](\\x,{-(\\x)^2-1})\n'
                'plot[domain=-2:2](\\x,{(\\x)^2+1});\n'
                '\\fill[green,smooth] (-1,0) --\n'
                'plot[domain=-1:1] (\\x,{(\\x)^2+1})\n'
                '-- (1,0) -- cycle;\n'
                '\\fill[green,smooth] (-1,0) --\n'
                'plot[domain=-1:1] (\\x,{-(\\x)^2-1})\n'
                '-- (1,0) -- cycle;\n'

                '\\fill[green,smooth]\n'
                'plot[domain=1:2] (\\x,{sqrt(\\x-1)})\n'
                '-- plot[domain=2:1] (\\x,{(\\x)^2+1})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=1:2] (\\x,{-sqrt(\\x-1)})\n'
                '-- plot[domain=2:1] (\\x,{-(\\x)^2-1})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-2:-1] (\\x,{-sqrt(-\\x-1)})\n'
                '-- plot[domain=-1:-2] (\\x,{-(\\x)^2-1})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-2:-1] (\\x,{sqrt(-\\x-1)})\n'
                '-- plot[domain=-1:-2] (\\x,{(\\x)^2+1})\n'
                '-- cycle;\n'

                '\\fill[green,smooth]\n'
                'plot[domain=2:5] (\\x,{sqrt(\\x-1)})\n'
                '-- plot[domain=5:2] (\\x,{5})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=2:5] (\\x,{-sqrt(\\x-1)})\n'
                '-- plot[domain=5:2] (\\x,{-5})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-5:-2] (\\x,{-sqrt(-\\x-1)})\n'
                '-- plot[domain=-2:-5] (\\x,{-5})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-5:-2] (\\x,{sqrt(-\\x-1)})\n'
                '-- plot[domain=-2:-5] (\\x,{5})\n'
                '-- cycle;\n'
                '\\node at (1,0) [left]{$I$};\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(a),latex(b),latex(h)))

                # Nội dung lời giải
                loigiai = ('Tính diện tích của một parabol bị khoét ở vị trí dưới cùng\\\\ \n'
                        'Chọn hệ trục tọa độ như hình vẽ\\\\ \n'
                        '\\begin{center}	\n'
                        '\\begin{tikzpicture}[scale=0.4] \n'
                        '\\draw[->] (-6,-5) -- (6,-5) node[below] {$x$}; \n'
                        '\\draw[->] (0,-6) -- (0,6) node[left] {$y$};\n'
                        '\\draw[dashed,red] (5,2)--(5,-2);\n'
                        '\\draw[dashed,red] (1,0)--(5,0);\n'
                        '\\node at (5,2) [right]{$A$};\n'
                        '\\node at (5,-2) [right]{$B$};\n'
                        '\\node at (5,0) [right]{$H$};\n'
                        '\\node at (0,-5) [above right]{$O$};\n'
                        '\\node at (2,-5) [below]{$%s$};\n'
                        '\\node at (-2,-5) [below]{$-%s$};\n'
                        '\\draw[samples=500]\n'
                'plot[domain=-5:-1](\\x,{sqrt(-\\x-1)})\n'
                'plot[domain=-5:-1](\\x,{-sqrt(-\\x-1)})\n'
                'plot[domain=1:5](\\x,{sqrt(\\x-1)})\n'
                'plot[domain=1:5](\\x,{-sqrt(\\x-1)})\n'
                'plot[domain=-2:2](\\x,{-(\\x)^2-1})\n'
                'plot[domain=-2:2](\\x,{(\\x)^2+1});\n'
                '\\fill[green,smooth] (-1,0) --\n'
                'plot[domain=-1:1] (\\x,{(\\x)^2+1})\n'
                '-- (1,0) -- cycle;\n'
                '\\fill[green,smooth] (-1,0) --\n'
                'plot[domain=-1:1] (\\x,{-(\\x)^2-1})\n'
                '-- (1,0) -- cycle;\n'

                '\\fill[green,smooth]\n'
                'plot[domain=1:2] (\\x,{sqrt(\\x-1)})\n'
                '-- plot[domain=2:1] (\\x,{(\\x)^2+1})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=1:2] (\\x,{-sqrt(\\x-1)})\n'
                '-- plot[domain=2:1] (\\x,{-(\\x)^2-1})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-2:-1] (\\x,{-sqrt(-\\x-1)})\n'
                '-- plot[domain=-1:-2] (\\x,{-(\\x)^2-1})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-2:-1] (\\x,{sqrt(-\\x-1)})\n'
                '-- plot[domain=-1:-2] (\\x,{(\\x)^2+1})\n'
                '-- cycle;\n'

                '\\fill[green,smooth]\n'
                'plot[domain=2:5] (\\x,{sqrt(\\x-1)})\n'
                '-- plot[domain=5:2] (\\x,{5})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=2:5] (\\x,{-sqrt(\\x-1)})\n'
                '-- plot[domain=5:2] (\\x,{-5})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-5:-2] (\\x,{-sqrt(-\\x-1)})\n'
                '-- plot[domain=-2:-5] (\\x,{-5})\n'
                '-- cycle;\n'
                '\\fill[green,smooth]\n'
                'plot[domain=-5:-2] (\\x,{sqrt(-\\x-1)})\n'
                '-- plot[domain=-2:-5] (\\x,{5})\n'
                '-- cycle;\n'
                '\\node at (1,0) [left]{$I$};\n'  
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Vì parabol nhận trục $Oy$ làm trục đối xứng và cắt $Oy$ tại điểm có tung độ bằng $%s$ nên có dạng $y=ax^2+%s$.\\\\ \n' 
                'Mặt khác parabol đi qua điểm $(%s;0)$ nên suy ra $y=%sx^2+%s$.\\\\ \n'
                'Diện tích một parabol bị khoét là\\\\ \n'
                '\\hspace*{1cm} $S_1=\\displaystyle\\int\\limits_{-%s}^{%s} \\left(%sx^2+%s\\right)\\text{d}x=%s$ cm$^2$.\\\\ \n'  
                'Diện tích miếng bìa hình vuông khi chưa bị khoét là\\\\ \n'
                '\\hspace*{1cm} $S_2=%s^2=%s$ cm$^2$.\\\\ \n'
                'Vậy diện tích phần hoa văn là\\\\ \n'
                '\\hspace*{1cm} $S=S_2-4S_1=%s-4\\cdot %s=%s$ cm$^2$.'    
                        %(latex(d),latex(d),latex(h),latex(h),
                            latex(d),latex(nsimplify(-h/d**2)),latex(h),
                            latex(d),latex(d),latex(nsimplify(-h/d**2)),latex(h),latex(nsimplify(k1-k2)),
                            latex(a),latex(a*a),latex(a*a),
                            latex(nsimplify(k1-k2)),latex(s)

                        ))



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

